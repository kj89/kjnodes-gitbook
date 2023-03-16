# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/bitcanna.png" width="150" alt=""><figcaption></figcaption></figure>

BitCanna is a proof-of-stake (POS) decentralized payment network designed exclusively to serve the cannabis industry. 

**Chain ID**: bitcanna-dev-1 | **Latest Version Tag**: v1.6.2 | **Wasm**: OFF

[Website](https://www.bitcanna.io) | [Discord](https://discord.gg/9AVrzaVQvs) | [Twitter](https://twitter.com/BitCannaGlobal)




## Chain explorer
[https://explorer.kjnodes.com/bitcanna-testnet](https://explorer.kjnodes.com/bitcanna-testnet)

## Public endpoints

* api: [https://bitcanna-testnet.api.kjnodes.com](https://bitcanna-testnet.api.kjnodes.com)
* rpc: [https://bitcanna-testnet.rpc.kjnodes.com](https://bitcanna-testnet.rpc.kjnodes.com)
* grpc: bitcanna-testnet.grpc.kjnodes.com:42090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@bitcanna-testnet.rpc.kjnodes.com:42656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@bitcanna-testnet.rpc.kjnodes.com:42659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/bitcanna-testnet/addrbook.json > $HOME/.bcna/config/addrbook.json
```

**live-peers** (0)
```bash
peers=""
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
