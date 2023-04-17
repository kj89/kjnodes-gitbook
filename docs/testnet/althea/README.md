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

**live-peers** (37)
```bash
peers="16a9576c9a4cf9651b4215e3a877ae002555dd9b@116.202.117.229:31656,eb69783b7e38059a58abaf342eb64f704de37636@23.88.66.239:31656,ba247bdf826a9636a8276d6a00d8004755f6bb18@162.19.238.210:26656,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,ff3fe47b494b0bf3dedf2d47dc9acf0e2ba3b7ae@65.108.43.113:52656,0037b2dc30933fa5c027a83be39f0061253ff83b@5.189.157.140:26656,698edcaf59b14f7bf50b681ef1ee3046fa062c77@65.109.92.235:11056,c1ad743c152d67dea9df71e3de2024cddd57c0cb@31.220.84.183:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,0d4220d2bbda711183a8db6f45c26b1541fa0d6a@65.109.116.204:21856,937dcf8c45b7c64e5188a7036427f2ce86383035@95.165.89.222:24126,5bad7ac6f006ee3b6f52dc91e85b5aae8e488233@194.163.149.53:26656,c1c28d02ef687f2d80b8e4540d9297835e75b6f0@139.59.67.156:26656,0aac1fc75b4a613f6bb7d15c6250350d478227a6@66.45.231.30:11144,c6e1ed7117cd56036cc51835945d155e9c474c01@144.76.17.123:26656,2cd7bd0bb40ed6f16ff7a9617ae8c7a74ce06e34@148.251.91.219:26656,4f3add677b0e4c8dec8b81101ea82620a19d5d0a@65.21.199.148:26633,ee22e048af133e8e83d594314a67b89be964eb37@138.201.225.104:47856,6c3d7683bf40a521b7c22391fd6c989b46a2e0e2@78.46.106.75:27656,cc542d9fb5f93780fc4004aa67f2b502686a24e8@144.76.27.79:61056,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886,11e8f38e3c5601e4ab2333d5a5bbb108a39b8e1c@159.69.110.238:26656,311a410a9c7dcf7d074f75ce52f882ebae3b1bb7@46.38.232.86:17656,79d18c52d35ddd204f61e9be8aa3c7b35d75cab7@65.108.139.20:26656,18643335ebbf1119ef5da9bbb2b65ce651a47ef1@5.9.106.214:26676,019988ce47565ad683b7675216e8fbcb171b841c@107.155.125.170:26656,cd71580f8ab4af6beeaf867702a86ca6f9331f71@65.19.136.133:23296,55a32dc9271d73279eaa3a5a58a88752d90a1ccf@95.217.58.111:28656,938388d1a011858d6238bf22944ab2dcba9b22a8@65.108.199.206:36656,26e70e13195b0d04cda0fca1f7b16b8746a620ed@65.109.28.226:26656,c7b642db1e41d4136d3fd36a6a505a3bcc504a2f@34.73.112.90:26656,3aeffaa1ac7b6741110987cfae4604751ac7d865@107.22.132.229:26656,c215cf295b05c1338fdf5070a7b2abde873f5a88@95.217.40.230:26656,90d692d481c1c4739ba8a7045b5552fa8d410901@88.99.164.158:17886,69a83a484a8e47a4a25f833aea64b3dbec51bb2b@65.19.136.130:26656,975393744d620d9dcb8dfd21c0282a6285766523@176.57.184.215:26656,5b6c6d679904ded86d36397e8ea583c122f5ddbd@144.91.102.95:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
