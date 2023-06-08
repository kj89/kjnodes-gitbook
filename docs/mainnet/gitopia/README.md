# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/gitopia.png" alt=""><figcaption></figcaption></figure>

Gitopia is the next-generation Code Collaboration Platform fuelled by  a decentralized network and interactive token economy. It is designed  to optimize the open-source software development process through  collaboration, transparency, and incentivization.

**Chain ID**: gitopia | **Latest Version Tag**: v2.1.1 | **Wasm**: OFF

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
peers="d25a718d491f52efdfd31e8dfdeaa69d1d1946dd@65.108.10.49:26556,082e95b5d5351e68dcfb24dff802f9064cfd5a4c@65.109.92.241:51056,e06b2be5c4ecee659e744da39d07b42f6f9e300c@192.99.44.79:11356,abca18ed112719b4f0a23932797dba2733f0fd44@23.88.5.169:25656,d724628333e34992ae0b46b7ae060cb31b06c1be@162.19.237.134:26656,4adfa5889675e1e91ea4459e15ff4a0ba53e7828@65.108.224.156:19656,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.140:27036,5e8a5481a314430e24de0919e18ffae394c269f6@51.159.221.31:26656,f9b892ea2e8ed8aa83f7b98e7e47371c23b01924@213.239.207.175:36656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:14156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
