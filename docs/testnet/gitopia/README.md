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
peers="fccf79904b3c03488955d580509d0cc65bb3bb56@65.21.104.192:26656,44a66336b029ba931165da3580cc6322af90339d@38.242.207.87:26656,80e7f845a187fabb8e361f749e34f034dfca3458@95.217.183.63:27656,0d1a964bbe844ab45a0ec93ffed81945e588f6b9@5.161.86.214:26656,f97115243c6291081b546e8d59f51e5ecede4168@149.102.155.225:26656,51c3b05112f73a6e60e8b2e96d5528a39a3f4e5e@38.242.246.96:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,98bdfc67810bf7ac8f5c45b2c677b4bf199eb42e@185.193.67.65:41656,075aa5cd1437de2a072878c347f9d4eb5849c842@86.48.5.165:26656,c19da021d6bbdeccdd03453a021d7171e6e299d5@173.249.14.30:656,599bb15403aae7679ba59f878ee8b9c39264fc93@185.213.25.129:60956,938ac1e4262cb2341bac323156fc3637f1b9c472@84.46.240.25:41656,b44d4fd0799d2c06fbec0257b376c0520bdb226a@185.250.37.147:41656,8e9c65f65157cd5540e94335ae068c4040cf9b3b@83.171.249.165:656,0d4c392f44c081347775643d99311bf2b36a7377@80.241.220.27:60956,66f94651fb02f277c90c605a38df549d3c0a9269@75.119.151.217:26656,458a98d6293064bdf3d6f86e0e2aa87bbb450f07@75.119.144.48:656,37c3d29df83da59e5a258d413e2f89365ab05711@85.239.243.12:656,95fbdc6d62be17db6688222b15b57d3e795ed07a@167.86.84.102:656,5ffdc1788f68df5e8163d9bd0d71a4c4d3dec2e9@81.0.220.21:26656,730983044bcc3f8e688bc2436da8a171fd843922@154.12.243.189:656,0c37cd47e46901caadd8288a158edb81d37427a0@209.126.6.101:26656,3b7845f8c8361c2f2de742473cd891c6e8cdeabf@83.171.249.159:656,f851ac3d5d06208bc52cf0ae86b090aa551c5659@80.85.141.82:26656,ff4fab3a07cdf3601b90ececd2de9a85b3a1a42e@82.208.21.152:26656,c820e754c56b5455d64ab7685730c44a936d0833@154.38.165.129:26656,ed9e3ea0d633fa27690f5d4db039403bbb1aeba8@165.22.214.209:26656,91bf3eb973595dd4621ccf5853e5ac78c48058da@194.163.180.77:656,8f4c2887e46edc200a95afeaa87cb63bdddd26e2@185.239.208.131:656,b30d41820868f19784589dce150f07e3bdce8ea2@86.48.0.95:26656,32254e5e11c49d8802f4c5bbd2c682eebd72ea33@80.241.220.28:60956,bfe5342ae808946452ed1ff21f5cb69f4f4bf78b@38.242.250.242:26656,c03e9f152bb1becc54d4424d02249135d39be09f@81.0.218.106:41656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,d159db085278927848c98b185b5871bf265669d9@185.250.36.169:41656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
