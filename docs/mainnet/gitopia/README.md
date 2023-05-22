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

**live-peers** (9)
```bash
peers="b2f764694d52e09793d68259d584ece0c194b6fe@65.108.229.93:26656,e8e6b032f408bcadc2e65f57c4376d91382104e8@135.181.209.55:26656,4adfa5889675e1e91ea4459e15ff4a0ba53e7828@65.108.224.156:19656,b89682dfddec974d867ea13817e90a444c21460c@138.201.127.91:26691,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:14156,d25a718d491f52efdfd31e8dfdeaa69d1d1946dd@65.108.10.49:26556,a2c24354d7d06e61266882a98b54e85800ac4b34@104.244.208.243:11356,c274f612fe7cf259aef7d9f01dc4ecfebca43656@148.251.137.146:26656,a5233e4359a39e09d7b261c200cdc014bbef76ad@65.108.8.247:11356"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
