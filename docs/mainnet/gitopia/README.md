# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/gitopia.png" alt=""><figcaption></figcaption></figure>

Gitopia is the next-generation Code Collaboration Platform fuelled by  a decentralized network and interactive token economy. It is designed  to optimize the open-source software development process through  collaboration, transparency, and incentivization.

**Chain ID**: gitopia | **Latest Version Tag**: v2.1.0 | **Wasm**: OFF

[Website](https://gitopia.com/) | [Discord](https://discord.gg/hFTXCGNYDZ) | [Twitter](https://twitter.com/gitopiaDAO)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/gitopia](https://explorer.kjnodes.com/gitopia)

## Public endpoints

* api: [https://gitopia.api.kjnodes.com](https://gitopia.api.kjnodes.com)
* rpc: [https://gitopia.rpc.kjnodes.com](https://gitopia.rpc.kjnodes.com)
* grpc: gitopia.grpc.kjnodes.com:14190

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@gitopia.rpc.kjnodes.com:14156
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@gitopia.rpc.kjnodes.com:14159
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/gitopia/addrbook.json > $HOME/.gitopia/config/addrbook.json
```

**live-peers** (10)
```bash
peers="d25a718d491f52efdfd31e8dfdeaa69d1d1946dd@65.108.10.49:26556,5b2df98ad73a0a81a5bd31da4489a9236a7d7a99@65.21.91.160:26867,382a5558ebb8493ca2a8057c51bc1b598520cf60@65.108.126.21:26656,abca18ed112719b4f0a23932797dba2733f0fd44@23.88.5.169:25656,5e8a5481a314430e24de0919e18ffae394c269f6@51.159.221.31:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.140:27036,de34c6491557c59bc5d73631fb73bf05cd726e3e@142.132.202.50:37656,0724a81eaee075bf4e1af702930dbc72977d71af@143.110.240.245:26656,b2f764694d52e09793d68259d584ece0c194b6fe@65.108.229.93:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:14156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
