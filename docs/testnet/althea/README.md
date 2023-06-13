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

**live-peers** (35)
```bash
peers="18643335ebbf1119ef5da9bbb2b65ce651a47ef1@5.9.106.214:26676,96320aaab7794933fddbc2bb101e54b8697c58e7@141.95.65.26:26656,31e4e58aed75f099eb5b71fd9fd48b48e4bf721a@5.75.170.207:26656,ccc09b0fb3c5f6b2dc826a6896bf43b099921bdb@207.180.253.242:26656,6d97969912514e3583dee8e0cca15a383adbde6c@213.246.57.175:26656,0037b2dc30933fa5c027a83be39f0061253ff83b@5.189.157.140:26656,ff3fe47b494b0bf3dedf2d47dc9acf0e2ba3b7ae@65.108.43.113:52656,79d18c52d35ddd204f61e9be8aa3c7b35d75cab7@65.108.139.20:26656,695f6de1a39a5f189015a50ef5f9df144a76b4d8@65.108.233.102:36656,5b6c6d679904ded86d36397e8ea583c122f5ddbd@144.91.102.95:26656,c215cf295b05c1338fdf5070a7b2abde873f5a88@95.217.40.230:26656,0d4220d2bbda711183a8db6f45c26b1541fa0d6a@65.109.116.204:21856,90d692d481c1c4739ba8a7045b5552fa8d410901@88.99.164.158:17886,76932bbeb29836c6405329c21358d051ef6e33a3@65.109.65.163:21856,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886,6c3d7683bf40a521b7c22391fd6c989b46a2e0e2@78.46.106.75:27656,0aac1fc75b4a613f6bb7d15c6250350d478227a6@66.45.231.30:11144,c1ad743c152d67dea9df71e3de2024cddd57c0cb@31.220.84.183:26656,8af3c5f2e975150cbf2d57bea182c2ca0fb808d2@65.21.237.170:10456,c5f4a56c4f1ba1cf3d4f8d787eb0f90d9cb963ec@65.109.34.133:61056,cd71580f8ab4af6beeaf867702a86ca6f9331f71@65.19.136.133:23296,11e8f38e3c5601e4ab2333d5a5bbb108a39b8e1c@159.69.110.238:26656,fd54b3d5e49c047dae61ca3a8e430f500eab783c@65.109.92.148:26656,70caf9545f6fd67f2561964b0a69bf36ba6f81d4@5.161.205.63:26656,975393744d620d9dcb8dfd21c0282a6285766523@176.57.184.215:26656,f6e3f995ba1c3ceed8bd556d9a23d2922d98a9a6@66.172.36.136:14656,24ae39234e1ceddc1585af9be8a6484edac79123@49.12.123.97:26656,13747f1f9960d19b72610cf7b59c2ec6d4eca27f@116.96.47.195:52656,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,937dcf8c45b7c64e5188a7036427f2ce86383035@95.165.89.222:24126,c831cd6ac278ab971eca94dda0c29191e8f39036@138.201.135.123:26656,c6e1ed7117cd56036cc51835945d155e9c474c01@144.76.17.123:26656,4ff3241de49fa01129b3fe38b3aeefc699f07cc7@42.119.159.212:26656,706f4ef87ae9c3b83fb48dcae1b10255f8f7dfa4@116.202.227.117:52656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
