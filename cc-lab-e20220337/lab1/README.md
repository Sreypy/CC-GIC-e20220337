# Lab 1: Amazon EC2 Walkthrough and Web Solution Challenge

**Student ID:** e20220337  
**Region:** us-east-1  

---

## Part 1.1 — Walkthrough: Bootstrapping an EC2 Instance

### 1. Security Group Configuration
![Security Group](images/01-security-group.jpg)

### 2. Key Pair Creation
![Key Pair](images/02-key-pair.jpg)

### 3. Instance Details (Running State)
![Instance Details](images/03-instance-details.jpg)

### 4. Browser Verification
![Browser Test](images/04-browser-test.jpg)

### 5. SSH Connection Output
![SSH Connection](images/05-ssh-connection.jpg)

---

## Part 1.2 — Challenge: EC2 Web Solution

### 1. Launch Configuration
![Challenge Launch](images/06-challenge-launch.jpg)

### 2. Challenge Security Group
![Challenge Security Group](images/07-challenge-security-group.jpg)

### 3. Running Challenge Instance
![Challenge Instance](images/08-challenge-instance.jpg)

### 4. Terminal Commands & Execution
![Challenge Terminal](images/09-challenge-terminal.jpg)

**Commands executed on instance:**
```bash
sudo dnf update -y
sudo dnf install -y httpd
sudo systemctl start httpd
sudo systemctl enable httpd
sudo systemctl status httpd --no-pager
echo "Welcome to the EC2 Challenge" | sudo tee /var/www/html/index.html
cat /var/www/html/index.html
df -h /