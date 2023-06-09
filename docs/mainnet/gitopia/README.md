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

**live-peers** (9)
```bash
peers="082e95b5d5351e68dcfb24dff802f9064cfd5a4c@65.109.92.241:51056,c274f612fe7cf259aef7d9f01dc4ecfebca43656@148.251.137.146:26656,de34c6491557c59bc5d73631fb73bf05cd726e3e@142.132.202.50:37656,1c90a7d16090e69fca5d53b6558b2cef7b8f88a8@116.203.35.46:36656,33e2390bfd693a8f2b27d5d646e0f081d717a81f@135.181.73.57:26656,e8e6b032f408bcadc2e65f57c4376d91382104e8@135.181.209.55:26656,b89682dfddec974d867ea13817e90a444c21460c@138.201.127.91:26691,f6bb45c38d0a9abc926b5baa8f27473f2cd37d30@141.95.157.139:11356,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:14156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
