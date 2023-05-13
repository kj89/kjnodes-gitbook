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

**live-peers** (37)
```bash
peers="cc542d9fb5f93780fc4004aa67f2b502686a24e8@144.76.27.79:61056,16a9576c9a4cf9651b4215e3a877ae002555dd9b@116.202.117.229:31656,cd71580f8ab4af6beeaf867702a86ca6f9331f71@65.19.136.133:23296,bcec1c0df99526be43efa248491b87e8a2374ebe@94.130.26.9:26956,695f6de1a39a5f189015a50ef5f9df144a76b4d8@65.108.233.102:36656,7eb055628aee375914d7d265ef4bc01ea692fe95@65.109.82.106:31656,a3ac64c5c84817f3694a866298399e6ad71ff26c@65.21.53.39:26656,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886,c7b642db1e41d4136d3fd36a6a505a3bcc504a2f@34.73.112.90:26656,c1c28d02ef687f2d80b8e4540d9297835e75b6f0@139.59.67.156:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,76932bbeb29836c6405329c21358d051ef6e33a3@65.109.65.163:21856,0d4220d2bbda711183a8db6f45c26b1541fa0d6a@65.109.116.204:21856,70caf9545f6fd67f2561964b0a69bf36ba6f81d4@5.161.205.63:26656,0aac1fc75b4a613f6bb7d15c6250350d478227a6@66.45.231.30:11144,fd54b3d5e49c047dae61ca3a8e430f500eab783c@65.109.92.148:26656,c215cf295b05c1338fdf5070a7b2abde873f5a88@95.217.40.230:26656,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,0037b2dc30933fa5c027a83be39f0061253ff83b@5.189.157.140:26656,8af3c5f2e975150cbf2d57bea182c2ca0fb808d2@65.21.237.170:10456,6c3d7683bf40a521b7c22391fd6c989b46a2e0e2@78.46.106.75:27656,04917b5810df2a380c1b18d83f577f1aba550818@222.106.187.14:53300,f6e3f995ba1c3ceed8bd556d9a23d2922d98a9a6@66.172.36.136:14656,ba247bdf826a9636a8276d6a00d8004755f6bb18@162.19.238.210:26656,bc55fa695313549672c4a480143dc400eaada16b@138.201.136.49:29656,938388d1a011858d6238bf22944ab2dcba9b22a8@65.108.199.206:36656,975393744d620d9dcb8dfd21c0282a6285766523@176.57.184.215:26656,15e7baf69c0db5c25e26cd1f13eb0d52a7a708b5@142.202.241.235:26656,5b6c6d679904ded86d36397e8ea583c122f5ddbd@144.91.102.95:26656,937dcf8c45b7c64e5188a7036427f2ce86383035@95.165.89.222:24126,a7b4e2ab0e3334bd2986c09cd5dafbc938ef23bf@65.108.78.101:52656,29dbc6241210d67e3460e2994e803bb2695dd71a@27.79.224.190:26656,4ff3241de49fa01129b3fe38b3aeefc699f07cc7@58.187.164.159:26656,90d692d481c1c4739ba8a7045b5552fa8d410901@88.99.164.158:17886,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:12456,9aa8a73ea9364aa3cf7806d4dd25b6aed88d8152@190.2.136.144:11356"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
