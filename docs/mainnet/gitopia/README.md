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
peers="4adfa5889675e1e91ea4459e15ff4a0ba53e7828@65.108.224.156:19656,f9b892ea2e8ed8aa83f7b98e7e47371c23b01924@213.239.207.175:36656,c274f612fe7cf259aef7d9f01dc4ecfebca43656@148.251.137.146:26656,e8e6b032f408bcadc2e65f57c4376d91382104e8@135.181.209.55:26656,f6bb45c38d0a9abc926b5baa8f27473f2cd37d30@141.95.157.139:11356,382a5558ebb8493ca2a8057c51bc1b598520cf60@65.108.126.21:26656,d724628333e34992ae0b46b7ae060cb31b06c1be@162.19.237.134:26656,b89682dfddec974d867ea13817e90a444c21460c@138.201.127.91:26691,e06b2be5c4ecee659e744da39d07b42f6f9e300c@192.99.44.79:11356,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:14156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
