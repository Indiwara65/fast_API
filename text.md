## for development the API can be run as a server by -              
	fastapi dev main.py                 
## path or endpoint              
	eg URL - https://example.com/items/foo                
	path - /items/foo                
	When developing a API "path" is the main way to seperate "concerns" and "resources"               
## CRUD                  
	C - Create (create data)                    
	R - Read (read data)              
	U - Update (update data)            
	D - Delete (delete data)     
## HTTP Methods
	A REST-API uses HTTP methods to accomplish CRUD.
	C - POST
	R - GET
	U - PUT
	D - DELETE
## HTTP Methods in Fast API
	POST - @app.post()
	GET  - @app.get()
	PUT  - @app.put()
	DELETE - @app.delete()
## TLS (Transport Layer Security)
	Transport layer security is used to encrypt the data that is been transfered between the client and the server.
 	A hand shake intially happens before the data transfer happens. 
  	Initially, the client sends a hello to the server it contains the TLS versions that the client handles and cipher suite.
   	Then the server presents the TLS certificate to the client with the public key.
    	Then, the client generated a pre master key which is encrypted using the public key and sent back to the server.
     	Then based on the pre master key and other data a master key is generated which will be used as the session key which will be used to encrypt the data transferd in the session.
	
