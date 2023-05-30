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
peers="d25a718d491f52efdfd31e8dfdeaa69d1d1946dd@65.108.10.49:26556,e06b2be5c4ecee659e744da39d07b42f6f9e300c@192.99.44.79:11356,4cf66531681c92f15c95c25bd1bff524f9dca35e@65.109.154.181:26656,0e9f303834a5d1f3be0babd5466725b3609ebc82@65.21.141.246:28656,382a5558ebb8493ca2a8057c51bc1b598520cf60@65.108.126.21:26656,d724628333e34992ae0b46b7ae060cb31b06c1be@162.19.237.134:26656,c274f612fe7cf259aef7d9f01dc4ecfebca43656@148.251.137.146:26656,de34c6491557c59bc5d73631fb73bf05cd726e3e@142.132.202.50:37656,f6bb45c38d0a9abc926b5baa8f27473f2cd37d30@141.95.157.139:11356,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:14156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
