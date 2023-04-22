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

**live-peers** (33)
```bash
peers="27dc32e6a756ccb04ca4e1395008f18f5efeaf8e@162.55.1.2:31656,bcec1c0df99526be43efa248491b87e8a2374ebe@94.130.26.9:26956,4f8729168c5454d04ff4a4d7b51986b2e97c68ff@165.232.104.13:26656,5df46d6901ca3487b640950cd0ffedd315536ca1@161.97.139.245:26656,a3ac64c5c84817f3694a866298399e6ad71ff26c@65.21.53.39:26656,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886,f6e3f995ba1c3ceed8bd556d9a23d2922d98a9a6@66.172.36.136:14656,0037b2dc30933fa5c027a83be39f0061253ff83b@5.189.157.140:26656,5b6c6d679904ded86d36397e8ea583c122f5ddbd@144.91.102.95:26656,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,0d4220d2bbda711183a8db6f45c26b1541fa0d6a@65.109.116.204:21856,76932bbeb29836c6405329c21358d051ef6e33a3@65.109.65.163:21856,c1d2d254a903b58692046b573dd06d2aa629266c@65.109.156.208:02656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,d5040e6aa2f190e04a39dc27e8199786a848e1cd@161.97.99.251:26156,cc542d9fb5f93780fc4004aa67f2b502686a24e8@144.76.27.79:61056,83147260a704b75283ca6da218516ee0eaa82956@170.64.156.36:26656,18643335ebbf1119ef5da9bbb2b65ce651a47ef1@5.9.106.214:26676,2f43ea489479761a7cb7e250b634706d2a441c27@94.19.249.187:29656,6d97969912514e3583dee8e0cca15a383adbde6c@213.246.57.175:26656,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,cd71580f8ab4af6beeaf867702a86ca6f9331f71@65.19.136.133:23296,311a410a9c7dcf7d074f75ce52f882ebae3b1bb7@46.38.232.86:17656,aa500219761eecd7f1f02a8bfd21c6dcdbd3cf42@142.132.232.40:26656,fd54b3d5e49c047dae61ca3a8e430f500eab783c@65.109.92.148:26656,4f3add677b0e4c8dec8b81101ea82620a19d5d0a@65.21.199.148:26633,ba247bdf826a9636a8276d6a00d8004755f6bb18@162.19.238.210:26656,937dcf8c45b7c64e5188a7036427f2ce86383035@95.165.89.222:24126,938388d1a011858d6238bf22944ab2dcba9b22a8@65.108.199.206:36656,0aac1fc75b4a613f6bb7d15c6250350d478227a6@66.45.231.30:11144,90d692d481c1c4739ba8a7045b5552fa8d410901@88.99.164.158:17886,c215cf295b05c1338fdf5070a7b2abde873f5a88@95.217.40.230:26656,93fa6dee174ed6f119223542ed0f622087adab7e@24.199.116.190:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
