#### **Database**
We need multiple types of db to handle different data efficiently.
We're gonna utilize the [**Polyglot Persistence Pattern**](https://en.wikipedia.org/wiki/Polyglot_persistence) like this:
	 - **Relational DB**
		A **relational database** like **PostgreSQL** (our choice) is ideal for structured interrelated data. Here, this would include: Users, Emails, Logs, etc.
	- **NoSQL DB**
		For storing dynamic, semi-structured data like our templates, it's better to use a NoSQL database like **MongoDB** or **Redis** (with JSON module).
			 **Why MongoDB?**
				- Great for storing and querying JSON-like documents.
				- Flexible schema lets you modify templates without altering the database structure.
				- Indexing and aggregation for querying template metadata.
			So, though Redis will provide extremely fast template retrieval (in the expense of less complex querying), I think MongoDB is a better option here.

We will also use **Docker** to containerize both databases for ease of deployment.

---
#### **Email Sending Mechanism**
We need a free self-hosted SMTP server like **Postfix**. For our MVP, the Gmail SMTP seems to be sufficient.
	**Multi-Sender Support**
		(From/Reply-To headers)
	**Domain Verification, DKIM, SPF**
		This ensures high deliverability.

**Note:** We may be able to use our internal main server for this part.

---
#### **Access Management**
A simple **Role-Based Access Control (RBAC)** implementation is sufficient.