
build:
	cd ..; docker build -t mygitlab/tokendealer -f docker/Dockerfile .

run:
	docker run --net=mygitlab --name=tokendealer -v /tmp/logs:/logs -p 8080:8080 -it mygitlab/tokendealer
