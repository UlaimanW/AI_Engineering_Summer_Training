# Day 4 – Prompt Patterns

---

## Role Prompting

### Prompt
```text
you are an expert cloud Engineer explain the main aws services to a coumputer scince student explain the couputer services and the storage services
```

### Output
```text
As a cloud engineer, I'd be happy to explain the main AWS services to you.

Compute Services:
These services allow you to run and manage compute resources in the cloud.

1. EC2 (Elastic Compute Cloud): Virtual servers in the cloud, where you can run your own operating system and applications.
2. Lambda: A serverless compute service that runs code in response to events, without provisioning or managing servers.
3. ECS (EC2 Container Service): A container orchestration service that allows you to run and manage Docker containers.
4. EKS (Elastic Container Service for Kubernetes): A managed Kubernetes service that allows you to run and manage containerized applications.

Storage Services:
These services provide a range of storage options for your data in the cloud.

1. S3 (Simple Storage Service): An object storage service that allows you to store and retrieve large amounts of data, such as files, images, and videos.
2. EBS (Elastic Block Store): A block-level storage service that provides persistent storage for your EC2 instances.
3. EFS (Elastic File System): A file-level storage service that provides a shared file system for your EC2 instances.
4. Glacier: A long-term archival storage service that allows you to store and retrieve data at a low cost.
```

### Notes
- This prompt assigns the model the role of an expert cloud engineer.
- It produced a broad explanation of AWS compute and storage services.

---

## Few-shot Prompting

### Prompt
```text
Here are examples of simple explanations for AWS compute services:

EC2:
Virtual servers in the cloud where you can run your own operating system and applications.

ECS:
A container orchestration service that lets you run and manage Docker containers.

Now explain this term in the same style:
Lambda
```

### Output
```text
Lambda: A serverless compute service that runs code without provisioning servers, scaling automatically in response to events.
```

### Notes
- This prompt gives the model examples first, then asks it to continue in the same style.
- The result followed the same short explanatory format.

---

## Chain-of-Thought Prompting

### Prompt
```text
Explain EC2 To a coumputer Science student think step by step define ec2 explain why they use it give one scenario where they use it
```

### Output
```text
Let's break down EC2 step by step:

What is EC2?
EC2 stands for Elastic Compute Cloud. It's a service provided by Amazon Web Services (AWS) that allows you to create and run virtual servers in the cloud.

Definition:
EC2 is a virtual machine that you can rent and use to run your own operating system and applications. Think of it like a remote computer that you can access and control over the internet.

Why use EC2?
Developers and businesses use EC2 for several reasons:
- Scalability
- Flexibility
- Cost-effectiveness

Scenario:
A web developer can use EC2 to host a website on a virtual Linux server and scale it later as traffic grows.
```

### Notes
- This prompt asks the model to explain the concept step by step.
- The answer was structured into definition, reasons for use, and a scenario.

---

## Structured Output Prompting

### Prompt
```text
Explain these AWS storage services to a computer science student: S3, EBS, and EFS.
Use this format for each service:
- Definition:
- Why it is used:
- Scenario:
Keep the whole answer under 120 words.
```

### Output
```text
S3: Object storage for files and data.
Used for: Storing and serving large files.
Scenario: Storing website images.

EBS: Block storage for EC2 instances.
Used for: Persistent data storage.
Scenario: Database storage.

EFS: File storage for EC2 instances.
Used for: Shared file systems.
Scenario: Shared project files.
```

### Notes
- This prompt forces the output into a fixed structure.
- The result was concise and easy to compare between services.
