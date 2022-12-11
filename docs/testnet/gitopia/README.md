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

**live-peers** (35)
```
peers="a6f4fd8efe8a575a15e25652ecebce3fa1ed62a0@213.239.217.52:35656,deca8c5aed2d1e617789d80927394a1d4d1c7360@149.102.146.123:26656,7182dfadba43a9a3b35f6862e63f75be20c8b1db@95.217.214.125:41656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,d9b86c9459ac8bb4760d37095732ccd2746aca1f@65.21.131.215:26356,599bb15403aae7679ba59f878ee8b9c39264fc93@185.213.25.129:60956,7a1c9ad925788a1811340b88068d6750c4511714@194.163.140.239:41656,c03e9f152bb1becc54d4424d02249135d39be09f@81.0.218.106:41656,8e9c65f65157cd5540e94335ae068c4040cf9b3b@83.171.249.165:656,cf31f6db36843f04675d694e6d79874d6acc3331@38.242.208.177:26656,3b7845f8c8361c2f2de742473cd891c6e8cdeabf@83.171.249.159:656,075aa5cd1437de2a072878c347f9d4eb5849c842@86.48.5.165:26656,0d4c392f44c081347775643d99311bf2b36a7377@80.241.220.27:60956,e79532749fb5dd95366f4568a7b2430d0e316fb5@84.46.255.163:26656,91bf3eb973595dd4621ccf5853e5ac78c48058da@194.163.180.77:656,96fc6a8c3eb58d43c4ac41e9e642ba8485837ad3@109.123.255.116:26656,b44d4fd0799d2c06fbec0257b376c0520bdb226a@185.250.37.147:41656,023c6a86fbd8b8368503c92bd612a8c0379a26e5@194.146.13.251:656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,42ba206efd9dd10847fa20f09a74fde6706442aa@194.146.13.128:60956,730983044bcc3f8e688bc2436da8a171fd843922@154.12.243.189:656,938ac1e4262cb2341bac323156fc3637f1b9c472@84.46.240.25:41656,32254e5e11c49d8802f4c5bbd2c682eebd72ea33@80.241.220.28:60956,0c37cd47e46901caadd8288a158edb81d37427a0@209.126.6.101:26656,c84906b19dc7dc7bda94ab2167d4b0af64a28b49@45.151.122.191:656,d159db085278927848c98b185b5871bf265669d9@185.250.36.169:41656,51c3b05112f73a6e60e8b2e96d5528a39a3f4e5e@38.242.246.96:26656,f4a2a6b840d1bad6f09c726d51f81d03f41c9ecc@194.146.13.246:656,66f94651fb02f277c90c605a38df549d3c0a9269@75.119.151.217:26656,61f824be9bdfe9a73b55ad162a9ed0bfe9121bbe@38.242.147.76:26656,b30d41820868f19784589dce150f07e3bdce8ea2@86.48.0.95:26656,eb5fee5e8d7d5a300db7c89a4a24a205197f85c5@185.237.97.56:656,ed9e3ea0d633fa27690f5d4db039403bbb1aeba8@165.22.214.209:26656,458a98d6293064bdf3d6f86e0e2aa87bbb450f07@75.119.144.48:656,f3289c45d545c589a4114aeeb364fa4c6fde08d9@109.123.254.216:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
