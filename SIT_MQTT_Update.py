#GUI
import tkinter as tk

#sysoutput
import os

#path
import sys

#sftp 
import paramiko

#checksum
import zlib
import binascii

#hash256
import hashlib

#process
import subprocess

# threading
import threading

#time
import datetime
import time 

def func_ssh( upload_file, dest_folder = "/run/media/mmcblk0p4/ftp_root/shared/", timeout_second = 10):
    
    remote_host = "10.0.0.1"
    remote_port = 8822
    remote_username = "root"
    remote_password = "Askey+1937"   
       
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(remote_host, port=remote_port, username=remote_username, password=remote_password, timeout = timeout_second )
    except paramiko.ssh_exception.SSHException as e:
        print(f"SSH connection failed: {e} \n")
        return ssh.close()

    sftp = ssh.open_sftp()
    if ssh.get_transport().is_active():
        None
    else: 
        print(f'Connect to {remote_host} fail')
        return sftp.close()
        
    # 上傳檔案
    transfer_result = sftp.put(upload_file, dest_folder + os.path.basename(upload_file))
    if transfer_result is not None:
        print(f"Upload file successfully \n {transfer_result} \n")
    else:
        print(f"Upload file failed: \n {transfer_result} \n")

    sftp.close()
    ssh.close()

def chksum_c(source_file, sha256_hash):
    n_checksum_mqtt_message = "{\"header\":{\"schemaName\":\"JSON\",\"magic\":\"\",\"timestamp\":{\"sec\":1628071772,\"nsec\":664227000},\"streamHandler\":{\"streamID\":0,\"seqNum\":0},\"chksum\":0},\"payloadType\":\"JSON\",\"payload\":{\"username\":\"mobileye\",\"password\":\"mobileye\",\"firmwareName\":\"" + source_file + "\",\"firmwareHash\":\"" + sha256_hash + "\"}}"
    payload_string = str(n_checksum_mqtt_message)
    # Print the checksum in hexadecimal format
    checksum = hex(zlib.crc32(n_checksum_mqtt_message.encode()))
    checksum_meg = checksum[:2] + checksum[2:].upper()
    return checksum_meg

def process_line(line):      
    if "Check Image" in line and "error\":\"none" in line:
        print("Check Image....\n")
    elif "Unpack" in line and "error\":\"none" in line:
        print("Unpack FOTA file....\n")            
    elif "Update SoC" in line and "error\":\"none" in line:
        print("UPDATE SOC....\n")
    elif "Update MCU" in line and "error\":\"none" in line:
        print("UPDATE MCU....\n")
    elif "Update MODEM" in line and "error\":\"none" in line:
        print("UPDATE MODEM....\n")

    return None

def recursive_process(proc, start_time):
    line = proc.stdout.readline().decode()
    if line:
        print(line)
        result = process_line(line)
        if result == "Finished" or result == "Update failed":
            return
        else:
            recursive_process(proc, start_time)

        print(time_counting(start_time))
    else:
        return

def time_counting(start_time):
    time_diff = datetime.datetime.now() - start_time
    return time_diff

def Main_MQTT_update(source_file, current_dir):

    os.chdir('OBU_Firmware')   

    #mqtt 
    mqtt_ad = "admin"
    mqtt_pwd = "admin"
    mqtt_ip = "10.0.0.1"
    port = 1883
    mqtt_topic = "TextCommand/Request/OTAFirmwareUpdate/v1/All/v1"
    id = "admin"
    def hash256(source_file):
        #hash python3.8
        with open(source_file, 'rb') as f:
            file_hash = hashlib.sha256()
            while chunk := f.read(8192):
                sha256_hash = file_hash.update(chunk)
            return sha256_hash
    
    def OTA_enable_setting():
        pub_topic_sftp = "TextCommand/Request/OTA/v1/Settings/v1"
        #enable SFTP & mqttupdate
        sftp_mqttupdate_message = "{\\\"header\\\":{\\\"schemaName\\\":\\\"JSON\\\",\\\"magic\\\":\\\"ef58ea3f-5559-466e-8b2d-6b9a3f000010\\\",\\\"timestamp\\\":{\\\"sec\\\":1628071772,\\\"nsec\\\":664227000},\\\"streamHandler\\\":{\\\"streamID\\\":0,\\\"seqNum\\\":0},\\\"chksum\\\":\\\"0x7E35B8FE\\\"},\\\"payloadType\\\":\\\"JSON\\\",\\\"payload\\\":{\\\"OTAFirmwareUpdateEnable\\\":true,\\\"localSFTPEnable\\\":true}}"
        sftp_update = f'mosquitto_pub.exe -u {mqtt_ad} -P {mqtt_pwd} -h {mqtt_ip} -t "{pub_topic_sftp}" -m "{sftp_mqttupdate_message}"'
        os.system(sftp_update)
        print(f"SFTP enable : \n {sftp_update} \n ")
   
    hash256(source_file)
    chksum_c(source_file, hash256(source_file))
    
    #BUpload file
    func_ssh(source_file) 

    #Sub
    def sub():
        sub_topic = "TextCommand/Response/OTAFirmwareUpdate/v1/All/v1"
        cmd_sub_start = f'mosquitto_sub.exe -u {mqtt_ad} -P {mqtt_pwd} -h {mqtt_ip} -t "{sub_topic}"'
        proc = subprocess.Popen(cmd_sub_start, shell=True, stdout=subprocess.PIPE)
        #start time
        start_time = datetime.datetime.now()
        recursive_process(proc, start_time)

    thread_sub = threading.Thread(target=sub)
    thread_sub.start()
    
#Set mqtt config
    mqtt_message = "{\\\"header\\\":{\\\"schemaName\\\":\\\"JSON\\\",\\\"magic\\\":\\\"\\\",\\\"timestamp\\\":{\\\"sec\\\":1628071772,\\\"nsec\\\":664227000},\\\"streamHandler\\\":{\\\"streamID\\\":0,\\\"seqNum\\\":0},\\\"chksum\\\":\\\"" + checksum_meg + "\\\"},\\\"payloadType\\\":\\\"JSON\\\",\\\"payload\\\":{\\\"username\\\":\\\"mobileye\\\",\\\"password\\\":\\\"mobileye\\\",\\\"firmwareName\\\":\\\"" + source_file + "\\\",\\\"firmwareHash\\\":\\\"" + sha256_hash + "\\\"}}"
    cmd = f'mosquitto_pub.exe -u {mqtt_ad} -P {mqtt_pwd} -h {mqtt_ip} -t "{mqtt_topic}" -m "{mqtt_message}"'
    print(f"Setup update config and data ....\n {cmd} \n ")
    os.system(cmd)

#START
    mqtt_start_message = "{\\\"header\\\":{\\\"schemaName\\\":\\\"JSON\\\",\\\"magic\\\":\\\"\\\",\\\"timestamp\\\":{\\\"sec\\\":1628071772,\\\"nsec\\\":664227000},\\\"streamHandler\\\":{\\\"streamID\\\":0,\\\"seqNum\\\":0},\\\"chksum\\\":\\\"0xCA2BFFF5\\\"},\\\"payloadType\\\":\\\"JSON\\\",\\\"payload\\\":{\\\"updateCmd\\\":\\\"start\\\"}}"
    print(f"START!!...\n {mqtt_start_message} \n")
    cmd_start = f'mosquitto_pub.exe -u {mqtt_ad} -P {mqtt_pwd} -h {mqtt_ip} -t "{mqtt_topic}" -m "{mqtt_start_message}"'
    os.system(cmd_start)
    #back to path
    os.chdir(current_dir)

def main():
    # save current dir path
    current_dir = os.getcwd()
    source_file = sys.argv[1]

    Main_MQTT_update(source_file, current_dir)
    
if __name__ == '__main__':
    main()