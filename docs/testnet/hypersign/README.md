# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/hypersign.png" width="150" alt=""><figcaption></figcaption></figure>

Hypersign is a decentralized identity layer for the internet, giving  users control of their personal data and identity whilst digital  enabling trust for businesses.

**Chain ID**: jagrat | **Latest Version Tag**: v0.1.6 | **Wasm**: OFF

[Website](https://hypersign.id) | [Discord](https://discord.gg/DmuUjMrHVw) | [Twitter](https://twitter.com/hypersignchain)




## Chain explorer
[https://explorer.kjnodes.com/hypersign-testnet](https://explorer.kjnodes.com/hypersign-testnet)

## Public endpoints

* api: [https://hypersign-testnet.api.kjnodes.com](https://hypersign-testnet.api.kjnodes.com)
* rpc: [https://hypersign-testnet.rpc.kjnodes.com](https://hypersign-testnet.rpc.kjnodes.com)
* grpc: [https://hypersign-testnet.grpc.kjnodes.com](https://hypersign-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@hypersign-testnet.rpc.kjnodes.com:31656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@hypersign-testnet.rpc.kjnodes.com:31659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/hypersign-testnet/addrbook.json > $HOME/.hid-node/config/addrbook.json
```

**live-peers** (32)
```bash
peers="934324c3b4318d8438954d19a82673a3d218951b@142.132.209.236:10956,001668e85c4f7b6ff796b3b593e485cd67223f0c@85.190.254.14:31656,1e3f0aeb6f2a2017b122af2461a75c9695790954@65.108.233.109:10956,bd2ae9f1c42183104719f7c44be078bb7d282a61@65.109.92.241:11056,ec5127072c252f7246fb66f7e7762423a23ff6bd@154.12.228.93:31656,56615e02aa90e35a20a1fc4c46e78bb00956f07b@192.118.76.199:26681,d92268c246e02a54103f7098b901b876c88f006e@5.161.130.108:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:31656,62c3f3e5214495593ad204f3c6cd879f3f4ed6a9@5.9.79.121:26656,9876d1b1e5b5968c1c729559325dd909f93c1d34@65.108.238.61:56656,fbc7ce82f02e24257395dc0310ad2921ea61e199@65.109.92.148:61156,eaf27acc810a3d6728dde972ebad26810cce0ae6@65.108.229.233:26656,1de2abae74a4c5fd7d96d9869ef02187f81498f0@134.209.238.66:26656,4e08d5b0cb43c8d5ffc42987a5166bab2a04a93b@65.109.92.240:21066,610843eda2f0388cb8e75917e8c1f63350bd3bd1@154.26.131.130:16656,ce6686036f6554deb0490103dcc201172e7c3f2f@81.0.220.131:26656,c90c48933111a74784e0dc8b28c5660acabc5788@185.196.20.153:26656,efcb16ec33d8e6233d1068fff679c6fd64bf5802@65.108.225.158:10956,d7c9b9a3c3a6c5f4ccdfb37a8358755b277271c1@3.110.226.164:26656,e003e628d5c748f2445f1731af20d461f585e7a5@182.253.224.66:12656,55b3cf307182091e60b774712733231a8cc7f448@89.163.132.156:31656,620478e35ba6740f0afb2a0dd6ca9b34765bc60e@65.109.30.12:60856,0c6758a3f4554bbc67da73993bbb697764c5c534@38.242.142.227:26656,d761b0e7bdaba0cbc223aaf728681d8018b764e4@83.171.249.114:28656,c1b6d86f46eab9d0aa2e4399cddb9cf05d13621a@65.108.206.118:60556,54f5df8d6516ead7099191776d9ee2048e0ec947@95.214.53.46:26656,84408be4e3f13dcd976568d6370e1c50e9eb614d@185.252.232.110:46656,d72875380d7b0b68f071623996bd5a86b7491287@116.202.227.117:31656,70f00c612c1d681a04244749a56f3a35e9be1420@65.108.194.40:28765,aa8c0064e866dc57b341a389006df8925a0718fe@5.161.55.130:31656,7ac746f53266043a92a05db06d1306b4e5f7e7c8@65.109.112.20:11014,a3f3d6dba11bfe080693938666064b2324fbaccf@88.99.164.158:11056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.hid-node/config/config.toml
```
