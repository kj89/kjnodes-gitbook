# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/gitopia.png" alt=""><figcaption></figcaption></figure>

Gitopia is the next-generation Code Collaboration Platform fuelled by  a decentralized network and interactive token economy. It is designed  to optimize the open-source software development process through  collaboration, transparency, and incentivization.

**Chain ID**: gitopia-janus-testnet-2 | **Latest Version Tag**: v1.2.0 | **Wasm**: OFF

[Website](https://gitopia.com/) | [Discord](https://discord.gg/hFTXCGNYDZ) | [Twitter](https://twitter.com/gitopiaDAO)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/gitopia-testnet](https://explorer.kjnodes.com/gitopia-testnet)

## Public endpoints

* api: [https://gitopia-testnet.api.kjnodes.com](https://gitopia-testnet.api.kjnodes.com)
* rpc: [https://gitopia-testnet.rpc.kjnodes.com](https://gitopia-testnet.rpc.kjnodes.com)
* grpc: gitopia-testnet.grpc.kjnodes.com:14190

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@gitopia-testnet.rpc.kjnodes.com:14156
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@gitopia-testnet.rpc.kjnodes.com:14159
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/gitopia-testnet/addrbook.json > $HOME/.gitopia/config/addrbook.json
```

**live-peers** (10)
```bash
peers="397cf4db87961e3a92f54b460300fc01d4dfa8f4@142.132.202.50:37656,c84906b19dc7dc7bda94ab2167d4b0af64a28b49@45.151.122.191:656,d84fbf48ce0773f207e8ab203d11ae644aa018df@65.108.192.123:17656,eccdf1d5bf33bc1733838562b4d4a4a45869c3a8@135.181.183.93:41656,f314268ef1886e4ad2801c8443ea0b0c8143a246@95.214.55.25:30656,5c74fe6868cda2003926c0a6299c9cebec5c4d1a@65.21.239.60:41656,03073657e8bc5bcf71e7fd8df281ab8dcbc8821a@45.151.122.130:656,f7fcda07044dc64cec2f6dca9da0c37a254bbae8@138.201.127.91:26676,023c6a86fbd8b8368503c92bd612a8c0379a26e5@194.146.13.251:656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
