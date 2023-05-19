# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/gitopia.png" alt=""><figcaption></figcaption></figure>

Gitopia is the next-generation Code Collaboration Platform fuelled by  a decentralized network and interactive token economy. It is designed  to optimize the open-source software development process through  collaboration, transparency, and incentivization.

**Chain ID**: gitopia | **Latest Version Tag**: v2.0.0 | **Wasm**: OFF

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
peers="bc959f28290e4e8ed76acdc4e0fc6b0911f1c512@135.181.208.166:26656,b89682dfddec974d867ea13817e90a444c21460c@138.201.127.91:26691,5e8a5481a314430e24de0919e18ffae394c269f6@51.159.221.31:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:14156,4adfa5889675e1e91ea4459e15ff4a0ba53e7828@65.108.224.156:19656,abca18ed112719b4f0a23932797dba2733f0fd44@23.88.5.169:25656,c274f612fe7cf259aef7d9f01dc4ecfebca43656@148.251.137.146:26656,b35d46fcfc1e4cfa943a299fcb39853e15e94d8b@81.30.157.35:14656,a5233e4359a39e09d7b261c200cdc014bbef76ad@65.108.8.247:11356,c35eb6124591bad21673e8d802898faa18e0352a@65.109.29.150:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
