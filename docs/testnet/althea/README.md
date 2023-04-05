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

**live-peers** (19)
```bash
peers="eab7a70812ba39094fc8bbf4f69f099123863b38@81.30.157.35:11656,5bad7ac6f006ee3b6f52dc91e85b5aae8e488233@194.163.149.53:26656,96320aaab7794933fddbc2bb101e54b8697c58e7@141.95.65.26:26656,698edcaf59b14f7bf50b681ef1ee3046fa062c77@65.109.92.235:11056,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,ff3fe47b494b0bf3dedf2d47dc9acf0e2ba3b7ae@65.108.43.113:52656,15e7baf69c0db5c25e26cd1f13eb0d52a7a708b5@142.202.241.235:26656,ba247bdf826a9636a8276d6a00d8004755f6bb18@162.19.238.210:26656,cd71580f8ab4af6beeaf867702a86ca6f9331f71@65.19.136.133:23296,8af3c5f2e975150cbf2d57bea182c2ca0fb808d2@65.21.237.170:10456,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,04917b5810df2a380c1b18d83f577f1aba550818@222.106.187.14:53300,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,2cd7bd0bb40ed6f16ff7a9617ae8c7a74ce06e34@148.251.91.219:26656,d320b861277a338daefec6e620daafe07fc5ee19@65.108.199.36:20036,ccc09b0fb3c5f6b2dc826a6896bf43b099921bdb@207.180.253.242:26656,695f6de1a39a5f189015a50ef5f9df144a76b4d8@65.108.233.102:36656,f6e3f995ba1c3ceed8bd556d9a23d2922d98a9a6@66.172.36.136:14656,3aeffaa1ac7b6741110987cfae4604751ac7d865@107.22.132.229:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
