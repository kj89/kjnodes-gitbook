# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/mars.png" width="150" alt=""><figcaption></figcaption></figure>

Mars is a credit protocol for the future: non-custodial,  open-source, transparent, algorithmic and community-governed.

**Chain ID**: ares-1 | **Latest Version Tag**: v1.0.0-rc7 | **Wasm**: ON

[Website](https://marsprotocol.io) | [Discord](https://discord.gg/marsprotocol) | [Twitter](https://twitter.com/mars_protocol)


## Public endpoints

* api: [https://mars-testnet.api.kjnodes.com](https://mars-testnet.api.kjnodes.com)
* rpc: [https://mars-testnet.rpc.kjnodes.com](https://mars-testnet.rpc.kjnodes.com)
* grpc: [https://mars-testnet.grpc.kjnodes.com](https://mars-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@mars-testnet.rpc.kjnodes.com:45656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@mars-testnet.rpc.kjnodes.com:45659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/mars-testnet/addrbook.json > $HOME/.mars/config/addrbook.json
```

**live-peers** (10)
```bash
peers="aea09eb8f366e388ca74e3f3ffe6909d5c89d1b9@95.214.55.155:22656,7f614946315d781fec92baf8cd6475fa6fea482a@65.109.92.148:61356,1eb8f66ad73bfaad455fa3c9711029a723367642@65.108.67.152:45656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:45656,59fdbead04db40a8bfcee1b42bc2351e1dc78d2e@207.180.243.64:36656,8d56c709c724b05d80fad790744f4b2255ffe90d@135.181.16.252:34656,c09e47ad29ea0421bc9cf073c4e104530f56a7ed@38.129.16.21:12,ef0736768c2f351c597c7307957a36de40209ef3@5.161.114.1:26656,70b4e6ad0c9c3a125acdec4ca47ac148c7e6f552@3.7.14.82:26656,bb2151bd2ffa6f5c93b6cad3d55aaee675a03ef4@161.97.79.100:56656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
