# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/althea.png" alt=""><figcaption></figcaption></figure>

Althea's unique cooperative vision for the internet  brings peering from the data center to the field

**Chain ID**: althea_7357-1 | **Latest Version Tag**: v0.3.2 | **Wasm**: OFF

[Website](https://www.althea.net) | [Discord](https://discord.gg/ZTKWfpDs) | [Twitter](https://twitter.com/altheanetwork)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/althea-testnet](https://explorer.kjnodes.com/althea-testnet)

## Public endpoints

* api: [https://althea-testnet.api.kjnodes.com](https://althea-testnet.api.kjnodes.com)
* rpc: [https://althea-testnet.rpc.kjnodes.com](https://althea-testnet.rpc.kjnodes.com)
* grpc: althea-testnet.grpc.kjnodes.com:15290

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@althea-testnet.rpc.kjnodes.com:15256
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@althea-testnet.rpc.kjnodes.com:15259
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/althea-testnet/addrbook.json > $HOME/.althea/config/addrbook.json
```

**live-peers** (41)
```bash
peers="bc55fa695313549672c4a480143dc400eaada16b@138.201.136.49:29656,2cd7bd0bb40ed6f16ff7a9617ae8c7a74ce06e34@148.251.91.219:26656,ccc09b0fb3c5f6b2dc826a6896bf43b099921bdb@207.180.253.242:26656,1991a3263255fc32d65b49335bcaee19f607c934@185.16.39.99:26656,7eb055628aee375914d7d265ef4bc01ea692fe95@65.109.82.106:31656,019988ce47565ad683b7675216e8fbcb171b841c@107.155.125.170:26656,d26fddea7ceb8cb5a52223702a23757cb09fad37@207.180.199.115:31656,04917b5810df2a380c1b18d83f577f1aba550818@222.106.187.14:53300,cc542d9fb5f93780fc4004aa67f2b502686a24e8@144.76.27.79:61056,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,0d4220d2bbda711183a8db6f45c26b1541fa0d6a@65.109.116.204:21856,76932bbeb29836c6405329c21358d051ef6e33a3@65.109.65.163:21856,d4c21f733f0aff703d36265b25126b01eaab8742@68.142.182.44:26656,c1c28d02ef687f2d80b8e4540d9297835e75b6f0@139.59.67.156:26656,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,cd71580f8ab4af6beeaf867702a86ca6f9331f71@65.19.136.133:23296,70caf9545f6fd67f2561964b0a69bf36ba6f81d4@5.161.205.63:26656,0aac1fc75b4a613f6bb7d15c6250350d478227a6@66.45.231.30:11144,733e9d5f995c2866df9f2e1254551940f060a70c@51.159.159.112:26656,ba247bdf826a9636a8276d6a00d8004755f6bb18@162.19.238.210:26656,16a9576c9a4cf9651b4215e3a877ae002555dd9b@116.202.117.229:31656,6c3d7683bf40a521b7c22391fd6c989b46a2e0e2@78.46.106.75:27656,dc67cbe058b802aa34f64715b44474c462b4317b@65.108.237.224:36656,698edcaf59b14f7bf50b681ef1ee3046fa062c77@65.109.92.235:11056,0037b2dc30933fa5c027a83be39f0061253ff83b@5.189.157.140:26656,a1c05be605625e7fd3af6b9e5c84937a48482be5@35.201.194.177:26656,c7b642db1e41d4136d3fd36a6a505a3bcc504a2f@34.73.112.90:26656,bcec1c0df99526be43efa248491b87e8a2374ebe@94.130.26.9:26956,fd54b3d5e49c047dae61ca3a8e430f500eab783c@65.109.92.148:26656,c58008ffca69359b3af57914c9f97b68c343f916@95.217.58.111:28656,4f3add677b0e4c8dec8b81101ea82620a19d5d0a@65.21.199.148:26633,975393744d620d9dcb8dfd21c0282a6285766523@176.57.184.215:26656,c831cd6ac278ab971eca94dda0c29191e8f39036@138.201.135.123:26656,15e7baf69c0db5c25e26cd1f13eb0d52a7a708b5@142.202.241.235:26656,ee22e048af133e8e83d594314a67b89be964eb37@138.201.225.104:47856,a590d26a6ad6629878aa88fec7283b7b3f7e7d45@5.189.157.124:36656,13747f1f9960d19b72610cf7b59c2ec6d4eca27f@116.96.44.135:52656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,766377592cbaae65d8e6df5120bd8b4fdfc8a372@98.63.20.2:26656,90d692d481c1c4739ba8a7045b5552fa8d410901@88.99.164.158:17886"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
