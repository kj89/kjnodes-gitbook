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
peers="eb5fee5e8d7d5a300db7c89a4a24a205197f85c5@185.237.97.56:656,0d1a964bbe844ab45a0ec93ffed81945e588f6b9@5.161.86.214:26656,5ffdc1788f68df5e8163d9bd0d71a4c4d3dec2e9@81.0.220.21:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,bfe5342ae808946452ed1ff21f5cb69f4f4bf78b@38.242.250.242:26656,d159db085278927848c98b185b5871bf265669d9@185.250.36.169:41656,c84906b19dc7dc7bda94ab2167d4b0af64a28b49@45.151.122.191:656,b44d4fd0799d2c06fbec0257b376c0520bdb226a@185.250.37.147:41656,72678266f62ab7f0e79acfe9579701f12693dd7a@185.216.75.69:41656,61f824be9bdfe9a73b55ad162a9ed0bfe9121bbe@38.242.147.76:26656,1d3bb209dfc7fe953fb8fa37774bab34016dd75c@185.245.183.85:26656,e79532749fb5dd95366f4568a7b2430d0e316fb5@84.46.255.163:26656,9cd6d2477d278ef6ccffa5cc4e22fd0d9489cd23@85.10.199.157:34656,51c3b05112f73a6e60e8b2e96d5528a39a3f4e5e@38.242.246.96:26656,deca8c5aed2d1e617789d80927394a1d4d1c7360@149.102.146.123:26656,075aa5cd1437de2a072878c347f9d4eb5849c842@86.48.5.165:26656,980e2ec8f4ddba44e4a928452e49f3cae722fce3@65.21.182.244:27656,c820e754c56b5455d64ab7685730c44a936d0833@154.38.165.129:26656,66f94651fb02f277c90c605a38df549d3c0a9269@75.119.151.217:26656,45de37d6340caef9bd84111ffb5163d0f3604e84@135.181.153.228:46656,6fa19dbe0236fc9328513ced95d9dd6f8330dbf3@34.160.118.165:26656,023c6a86fbd8b8368503c92bd612a8c0379a26e5@194.146.13.251:656,1989ced6b71ce676a5ab4d0586d85e38fd41fbd2@136.243.88.91:7070,f4a2a6b840d1bad6f09c726d51f81d03f41c9ecc@194.146.13.246:656,458a98d6293064bdf3d6f86e0e2aa87bbb450f07@75.119.144.48:656,8e9c65f65157cd5540e94335ae068c4040cf9b3b@83.171.249.165:656,3b7845f8c8361c2f2de742473cd891c6e8cdeabf@83.171.249.159:656,f97115243c6291081b546e8d59f51e5ecede4168@149.102.155.225:26656,730983044bcc3f8e688bc2436da8a171fd843922@154.12.243.189:656,0c31077af45cb4f0424e58c91b0a917c36a90fd9@65.108.195.235:16656,91bf3eb973595dd4621ccf5853e5ac78c48058da@194.163.180.77:656,7a1c9ad925788a1811340b88068d6750c4511714@194.163.140.239:41656,481189b7e246f6c824a969482446c49abbfe76b8@161.97.172.147:26656,d0ca7d1e144eee74396b1c7a98737e4ca2ced2bb@137.184.30.252:656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
