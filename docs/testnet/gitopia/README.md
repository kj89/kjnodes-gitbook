# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gitopia.png" width="150" alt=""><figcaption></figcaption></figure>

Gitopia is the next-generation Code Collaboration Platform fuelled by  a decentralized network and interactive token economy. It is designed  to optimize the open-source software development process through  collaboration, transparency, and incentivization.

**Chain ID**: gitopia-janus-testnet-2 | **Latest Version Tag**: v1.2.0 | **Wasm**: OFF

Website: [https://gitopia.com/](https://gitopia.com/)


## Public endpoints

* rpc: [https://gitopia-testnet.rpc.kjnodes.com](https://gitopia-testnet.rpc.kjnodes.com)
* api: [https://gitopia-testnet.api.kjnodes.com](https://gitopia-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@gitopia-testnet.rpc.kjnodes.com:41656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@gitopia-testnet.rpc.kjnodes.com:41659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/gitopia-testnet/addrbook.json > $HOME/.gitopia/config/addrbook.json
```

**live-peers** (27)
```
peers="76895e84873db23aa366296acc6900e1dd980f43@195.201.237.185:22656,4977214dacb3713797653c1bc07b5982bcc91649@142.132.253.112:51656,d159db085278927848c98b185b5871bf265669d9@185.250.36.169:41656,67e839cff368a20c9b7a1390b739d3538866b0b6@65.21.134.202:26356,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,d9b86c9459ac8bb4760d37095732ccd2746aca1f@65.21.131.215:26356,75a9570b82474af11fc8c895f9da1ecb5da0c73f@95.216.143.237:19656,965e495f4a69294bd85f3437fccdc9b210fd98b6@1.15.146.92:26656,72678266f62ab7f0e79acfe9579701f12693dd7a@185.216.75.69:41656,8a20f16d02806ba11bf9fab1fca91830578faa9e@161.97.151.46:46656,7a1c9ad925788a1811340b88068d6750c4511714@194.163.140.239:41656,2f58a44c9ce9dcdf81e2eaed7cd808ebefe222a7@38.242.243.111:26656,f91f270980654a74c7619eff18bc068d2b86e6d8@54.90.149.14:41656,e53572d91ae5c25caf23b6390467d1d2978ae3b7@65.109.14.17:26656,6fa19dbe0236fc9328513ced95d9dd6f8330dbf3@34.160.118.165:26656,fbd3b296871ae841b638158e29d48e09180b7c4e@194.233.77.238:41656,c820e754c56b5455d64ab7685730c44a936d0833@154.38.165.129:26656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,96fc6a8c3eb58d43c4ac41e9e642ba8485837ad3@109.123.255.116:26656,6a7ba7eca935a76e02b5bbb9caf149a41da9af12@144.76.27.79:46656,075aa5cd1437de2a072878c347f9d4eb5849c842@86.48.5.165:26656,1989ced6b71ce676a5ab4d0586d85e38fd41fbd2@136.243.88.91:7070,dea00215e54c4098a4f194a7ecd43e24ea99336f@88.99.95.81:26656,bbc6a1e115185d5bffcbbf5520dca1c3d626e599@109.123.255.50:26656,7e0534cc92832ce8b499ffc662a9b73d2c0351a6@135.181.162.138:27001,f4a2a6b840d1bad6f09c726d51f81d03f41c9ecc@194.146.13.246:656,d2291c87bdef89c31f8e4008ddc0dee2d2a8ef50@143.244.182.43:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
