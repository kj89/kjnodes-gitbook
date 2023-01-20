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
peers="ed6bc9782a9cf2f5c302d8ecd5c53c27a3413e96@65.109.88.155:43656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:45656,92c3c938d39362d743c3d621619642fc81d5eb0e@91.230.110.200:45656,7f614946315d781fec92baf8cd6475fa6fea482a@65.109.92.148:61356,0d03b322852add71896c6bbf0010e68410b45ac3@37.187.144.187:32656,ef0736768c2f351c597c7307957a36de40209ef3@5.161.114.1:26656,fe8d614aa5899a97c11d0601ef50c3e7ce17d57b@65.108.233.109:18556,934c311b462b889c2e9899fcd42e3523896d2548@65.108.97.58:2866,a446002f40b926db596deb7bae9ed3fe04af1c2e@65.108.206.215:17656,5dac2a64e4aea39e3704d551441938a504134e95@194.113.106.81:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
