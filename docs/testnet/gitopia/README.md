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

**live-peers** (34)
```
peers="4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,c820e754c56b5455d64ab7685730c44a936d0833@154.38.165.129:26656,023c6a86fbd8b8368503c92bd612a8c0379a26e5@194.146.13.251:656,0c31077af45cb4f0424e58c91b0a917c36a90fd9@65.108.195.235:16656,f97115243c6291081b546e8d59f51e5ecede4168@149.102.155.225:26656,5ffdc1788f68df5e8163d9bd0d71a4c4d3dec2e9@81.0.220.21:26656,bbc6a1e115185d5bffcbbf5520dca1c3d626e599@109.123.255.50:26656,deca8c5aed2d1e617789d80927394a1d4d1c7360@149.102.146.123:26656,eb5fee5e8d7d5a300db7c89a4a24a205197f85c5@185.237.97.56:656,66f94651fb02f277c90c605a38df549d3c0a9269@75.119.151.217:26656,730983044bcc3f8e688bc2436da8a171fd843922@154.12.243.189:656,8e9c65f65157cd5540e94335ae068c4040cf9b3b@83.171.249.165:656,bfe5342ae808946452ed1ff21f5cb69f4f4bf78b@38.242.250.242:26656,96fc6a8c3eb58d43c4ac41e9e642ba8485837ad3@109.123.255.116:26656,0d1a964bbe844ab45a0ec93ffed81945e588f6b9@5.161.86.214:26656,a6f4fd8efe8a575a15e25652ecebce3fa1ed62a0@213.239.217.52:35656,72678266f62ab7f0e79acfe9579701f12693dd7a@185.216.75.69:41656,c84906b19dc7dc7bda94ab2167d4b0af64a28b49@45.151.122.191:656,f91f270980654a74c7619eff18bc068d2b86e6d8@54.90.149.14:41656,91bf3eb973595dd4621ccf5853e5ac78c48058da@194.163.180.77:656,075aa5cd1437de2a072878c347f9d4eb5849c842@86.48.5.165:26656,3b7845f8c8361c2f2de742473cd891c6e8cdeabf@83.171.249.159:656,61f824be9bdfe9a73b55ad162a9ed0bfe9121bbe@38.242.147.76:26656,0cccef180d7597bbeef7d2b80d52913ab205879f@65.108.193.133:26656,2f58a44c9ce9dcdf81e2eaed7cd808ebefe222a7@38.242.243.111:26656,e79532749fb5dd95366f4568a7b2430d0e316fb5@84.46.255.163:26656,d159db085278927848c98b185b5871bf265669d9@185.250.36.169:41656,458a98d6293064bdf3d6f86e0e2aa87bbb450f07@75.119.144.48:656,67e839cff368a20c9b7a1390b739d3538866b0b6@65.21.134.202:26356,6fa19dbe0236fc9328513ced95d9dd6f8330dbf3@34.160.118.165:26656,7182dfadba43a9a3b35f6862e63f75be20c8b1db@95.217.214.125:41656,32254e5e11c49d8802f4c5bbd2c682eebd72ea33@80.241.220.28:60956,d86665c7f69a55bc6b4daf9d4629a082c20e52ad@95.216.199.56:35656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
