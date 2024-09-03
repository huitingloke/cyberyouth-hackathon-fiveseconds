const emailList = document.querySelector('.email-list');

const emails = [
  {
    subject: 'Hello from John',
    sender: 'john@example.com',
    date: '2024-09-03',
    malicious: false
  },
  {
    subject: ' Urgent: Update Your Password',
    sender: 'support@example.com',
    date: '2024-09-02',
    malicious: true
  },
  {
    subject: 'Meeting Invitation',
    sender: 'jane@example.com',
    date: '2024-09-01',
    malicious: false
  }
];

emails.forEach((email) => {
  const emailItem = document.createElement('div');
  emailItem.className = 'email-item';

  const subjectSpan = document.createElement('span');
  subjectSpan.className = 'email-subject';
  subjectSpan.textContent = email.subject;

  const senderSpan = document.createElement('span');
  senderSpan.className = 'email-sender';
  senderSpan.textContent = email.sender;

  const dateSpan = document.createElement('span');
  dateSpan.className = 'email-date';
  dateSpan.textContent = email.date;

  if (email.malicious) {
    const maliciousFlag = document.createElement('span');
    maliciousFlag.className = 'malicious-flag';
    maliciousFlag.textContent = '!';
    emailItem.appendChild(maliciousFlag);
  }

  emailItem.appendChild(subjectSpan);
  emailItem.appendChild(senderSpan);
  emailItem.appendChild(dateSpan);

  emailList.appendChild(emailItem);
});
