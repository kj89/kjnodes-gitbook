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

**live-peers** (36)
```bash
peers="16a9576c9a4cf9651b4215e3a877ae002555dd9b@116.202.117.229:31656,ccc09b0fb3c5f6b2dc826a6896bf43b099921bdb@207.180.253.242:26656,ba247bdf826a9636a8276d6a00d8004755f6bb18@162.19.238.210:26656,eab7a70812ba39094fc8bbf4f69f099123863b38@81.30.157.35:11656,bdf94092f6dc380f6526f7b8b46b63192e95a033@173.212.222.167:29656,c1ad743c152d67dea9df71e3de2024cddd57c0cb@31.220.84.183:26656,4f3add677b0e4c8dec8b81101ea82620a19d5d0a@65.21.199.148:26633,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886,76932bbeb29836c6405329c21358d051ef6e33a3@65.109.65.163:21856,0bc9489b1c93615e44410c1d9cc72c7f538cc802@51.81.208.203:11656,0d4220d2bbda711183a8db6f45c26b1541fa0d6a@65.109.116.204:21856,70caf9545f6fd67f2561964b0a69bf36ba6f81d4@5.161.205.63:26656,0aac1fc75b4a613f6bb7d15c6250350d478227a6@66.45.231.30:11144,2cd7bd0bb40ed6f16ff7a9617ae8c7a74ce06e34@148.251.91.219:26656,937dcf8c45b7c64e5188a7036427f2ce86383035@95.165.89.222:24126,a1c05be605625e7fd3af6b9e5c84937a48482be5@35.201.194.177:26656,c5f4a56c4f1ba1cf3d4f8d787eb0f90d9cb963ec@65.109.34.133:61056,0037b2dc30933fa5c027a83be39f0061253ff83b@5.189.157.140:26656,695f6de1a39a5f189015a50ef5f9df144a76b4d8@65.108.233.102:36656,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,fd54b3d5e49c047dae61ca3a8e430f500eab783c@65.109.92.148:26656,27dc32e6a756ccb04ca4e1395008f18f5efeaf8e@162.55.1.2:31656,ee22e048af133e8e83d594314a67b89be964eb37@138.201.225.104:47856,c7b642db1e41d4136d3fd36a6a505a3bcc504a2f@34.73.112.90:26656,382264d78149b62e679bf6d0b93dc74dd033fc05@65.108.2.41:26656,96320aaab7794933fddbc2bb101e54b8697c58e7@141.95.65.26:26656,975393744d620d9dcb8dfd21c0282a6285766523@176.57.184.215:26656,6c3d7683bf40a521b7c22391fd6c989b46a2e0e2@78.46.106.75:27656,93fa6dee174ed6f119223542ed0f622087adab7e@24.199.116.190:26656,c831cd6ac278ab971eca94dda0c29191e8f39036@138.201.135.123:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,8af3c5f2e975150cbf2d57bea182c2ca0fb808d2@65.21.237.170:10456,90d692d481c1c4739ba8a7045b5552fa8d410901@88.99.164.158:17886,766377592cbaae65d8e6df5120bd8b4fdfc8a372@98.63.20.2:26656,5df46d6901ca3487b640950cd0ffedd315536ca1@161.97.139.245:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
