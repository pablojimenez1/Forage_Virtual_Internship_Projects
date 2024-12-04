# AIG Cybersecurity Job Simulation


## Objective
To simulate real-world cybersecurity scenarios by responding to critical threats and ransomware attacks. The goal was to identify and mitigate a zero-day vulnerability, as well as recover encrypted files from a ransomware attack using Python brute force techniques.


### Skills Learned
- Vulnerability assessment and research.
- Communication with technical teams regarding cyber threats.
- Email drafting for security incidents, including threat notification and remediation guidance.
- Python scripting for cybersecurity purposes, specifically brute-force decryption.
- Incident response techniques.
- Risk mitigation and decision-making in critical cybersecurity situations.

### Tools Used
- Python: For scripting and brute-forcing the ransomware decryption key.
- CISA Publications: To gather information about the zero-day vulnerability.
- Encryption/Decryption Tools: For handling the ransomware-encrypted file.
- Email Client: For drafting and sending the vulnerability notification.

## Steps

Task 1: Responding to a zero-day vulnerability - Review recent publications from the Cybersecurity & Infrastructure Security Agency (CISA), research the reported vulnerability, and draft an email to the affected teams to notify them of the vulnerability and provide remediation guidance. 

- As an Information Security Analyst in the Cyber & Information Security Team, my common task and responsibility is to stay on top of emerging vulnerabilities to make sure that the company can remediate them before an attacker can exploit them.

The CISA has recently published the following two advisories:

- The [first advisory (Log4j)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-356a) outlines a serious vulnerability in one of the world’s most popular logging software. 
- The [second advisory](https://www.cisa.gov/news-events/news/cisa-fbi-nsa-and-international-partners-issue-advisory-ransomware-trends-2021) explores how ransomware has been increasing and is becoming professionalized - a concern for a large company like AIG.
  
We need to respond to the Apache Log4j zero-day vulnerability that was released to the public by advising affected teams of the vulnerability. So, we conduct the research on the vulnerability using the “CISA Advisory" resources provided above as a starting point. Visiting the above link, I found the important information:

*Ref 1.1: Apache Log4j*
<img width="900" alt="T1-CISA1" src="https://github.com/user-attachments/assets/630369dc-a65a-4ca7-8efa-b1aa43e3d45a">
<img width="900" alt="T1-CISA2" src="https://github.com/user-attachments/assets/b720fb5a-a27c-44af-9070-8c74f8f2a6e2">

Afterward, we analyze the AIG Infrastructure List below to find out which infrastructure may be affected by the vulnerability, and which team has ownership.


*Ref 1.2: Infrastructure List*
<img width="900" alt="T1-Infrastructure List" src="https://github.com/user-attachments/assets/aead8685-6853-4dcb-b891-201f7bc37181">

Based on the above infrastructure list, the "Product Development Team" is using Apache Log4j services. Finally, we draft an advisory email to alert the infrastructure owner of the seriousness of this vulnerability. 

*Ref 1.3: Email*
<img width="502" alt="AIGTask1" src="https://github.com/user-attachments/assets/bea11dd2-7a81-4b16-9854-7e572c8b791d">

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Task 2 -Bypassing ransomware - Bruteforce the decryption key for a zip file encrypted by a ransomware virus. The attacker exploited a vulnerability but only managed to encrypt one file before the Incident Detection & Response team intervened. Given the attacker's use of copy-pasted payloads and their lack of lateral movement, the encryption key is expected to be simple. The Chief Information Security Officer has opted not to pay the ransom, so you are tasked with recovering the file by cracking the decryption key.

*Ref 2.1: Encrypted File*

<img width="551" alt="AIGTask2EncryptedFile" src="https://github.com/user-attachments/assets/80967c5a-0951-4525-ae24-a12544c20f6b">



- In this task, we will write a Python script to bruteforce the decryption key of the encrypted file. We will use Rockyou - a widely known password wordlist that contains thousands of common passwords in one wordlist to try to break the password encryption. After numerous attempts, we were successful in decrypting the password - "SPONGEBOB' and retrieving the file.


*Ref 2.2: Decrypting File*
![image](https://github.com/user-attachments/assets/1751ddaf-8502-4e49-b2b0-fbe8e9eaf07c)

![image](https://github.com/user-attachments/assets/475f3949-aa71-469d-a338-0060508d5b7d)

## Certificate
![image](https://github.com/user-attachments/assets/14ba3c3c-6a20-4ee6-be60-1f3877891ef0)


### Conclusion
This project provided hands-on experience in managing two critical cybersecurity incidents: addressing a zero-day vulnerability and responding to a ransomware attack. Through the simulation, I learned how to assess vulnerabilities, communicate security threats effectively, and apply technical skills to decrypt ransomware-encrypted files. This experience highlighted the importance of proactive incident response, strong communication, and the technical know-how to mitigate risks in a corporate environment.
