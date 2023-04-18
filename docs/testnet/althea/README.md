# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/althea.png" width="150" alt=""><figcaption></figcaption></figure>

Althea's unique cooperative vision for the internet  brings peering from the data center to the field

**Chain ID**: althea_7357-1 | **Latest Version Tag**: v0.3.2 | **Wasm**: OFF

[Website](https://www.althea.net) | [Discord](https://discord.gg/ZTKWfpDs) | [Twitter](https://twitter.com/altheanetwork)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/althea-testnet](https://explorer.kjnodes.com/althea-testnet)

## Public endpoints

* api: [https://althea-testnet.api.kjnodes.com](https://althea-testnet.api.kjnodes.com)
* rpc: [https://althea-testnet.rpc.kjnodes.com](https://althea-testnet.rpc.kjnodes.com)
* grpc: althea-testnet.grpc.kjnodes.com:52090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@althea-testnet.rpc.kjnodes.com:52656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@althea-testnet.rpc.kjnodes.com:52659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/althea-testnet/addrbook.json > $HOME/.althea/config/addrbook.json
```

**live-peers** (35)
```bash
peers="18643335ebbf1119ef5da9bbb2b65ce651a47ef1@5.9.106.214:26676,ba247bdf826a9636a8276d6a00d8004755f6bb18@162.19.238.210:26656,27dc32e6a756ccb04ca4e1395008f18f5efeaf8e@162.55.1.2:31656,5b6c6d679904ded86d36397e8ea583c122f5ddbd@144.91.102.95:26656,0037b2dc30933fa5c027a83be39f0061253ff83b@5.189.157.140:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,5bad7ac6f006ee3b6f52dc91e85b5aae8e488233@194.163.149.53:26656,a51b45869b5403dc71251a69879c1eb1c3042bed@65.108.134.215:29336,937dcf8c45b7c64e5188a7036427f2ce86383035@95.165.89.222:24126,c1c28d02ef687f2d80b8e4540d9297835e75b6f0@139.59.67.156:26656,0d4220d2bbda711183a8db6f45c26b1541fa0d6a@65.109.116.204:21856,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,c1d2d254a903b58692046b573dd06d2aa629266c@65.109.156.208:02656,0aac1fc75b4a613f6bb7d15c6250350d478227a6@66.45.231.30:11144,c831cd6ac278ab971eca94dda0c29191e8f39036@138.201.135.123:26656,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,24ae39234e1ceddc1585af9be8a6484edac79123@49.12.123.97:26656,311a410a9c7dcf7d074f75ce52f882ebae3b1bb7@46.38.232.86:17656,cc542d9fb5f93780fc4004aa67f2b502686a24e8@144.76.27.79:61056,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886,5df46d6901ca3487b640950cd0ffedd315536ca1@161.97.139.245:26656,d5040e6aa2f190e04a39dc27e8199786a848e1cd@161.97.99.251:26156,aa500219761eecd7f1f02a8bfd21c6dcdbd3cf42@142.132.232.40:26656,ccc09b0fb3c5f6b2dc826a6896bf43b099921bdb@207.180.253.242:26656,2cd7bd0bb40ed6f16ff7a9617ae8c7a74ce06e34@148.251.91.219:26656,16a9576c9a4cf9651b4215e3a877ae002555dd9b@116.202.117.229:31656,76932bbeb29836c6405329c21358d051ef6e33a3@65.109.65.163:21856,019988ce47565ad683b7675216e8fbcb171b841c@107.155.125.170:26656,bcec1c0df99526be43efa248491b87e8a2374ebe@94.130.26.9:26956,975393744d620d9dcb8dfd21c0282a6285766523@176.57.184.215:26656,22e7abeb10ac7042bce01c18d08958d9f3962a30@65.108.225.158:12456,4a8c845bdffc8bae0ed0e91a476bc57720adec15@65.108.206.74:26656,04917b5810df2a380c1b18d83f577f1aba550818@222.106.187.14:53300,90d692d481c1c4739ba8a7045b5552fa8d410901@88.99.164.158:17886,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:12456"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
