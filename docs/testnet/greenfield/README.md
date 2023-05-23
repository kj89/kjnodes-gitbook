# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/greenfield.png" alt=""><figcaption></figcaption></figure>

BNB Greenfield is an innovative blockchain and storage  platform that seeks to unleash the power of decentralized  technology on data ownership and the data economy

**Chain ID**: greenfield_5600-1 | **Latest Version Tag**: v0.1.1 | **Wasm**: OFF

[Website](https://greenfield.bnbchain.org) | [Discord](https://discord.gg/bnbchain) | [Twitter](https://twitter.com/BNBChain)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/greenfield-testnet](https://explorer.kjnodes.com/greenfield-testnet)

## Public endpoints

* api: [https://greenfield-testnet.api.kjnodes.com](https://greenfield-testnet.api.kjnodes.com)
* rpc: [https://greenfield-testnet.rpc.kjnodes.com](https://greenfield-testnet.rpc.kjnodes.com)
* grpc: greenfield-testnet.grpc.kjnodes.com:15490

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@greenfield-testnet.rpc.kjnodes.com:15456
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@greenfield-testnet.rpc.kjnodes.com:15459
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/greenfield-testnet/addrbook.json > $HOME/.gnfd/config/addrbook.json
```

**live-peers** (3)
```bash
peers="20c3e15d8dcc3988f533dd456a55d4584b2e78f6@131.153.158.3:26656,7a635c262955a2e85c654615f390f3a3e9c71328@54.225.72.119:26656,f811d0f87415bcc5daba37ec925b137a1b403372@35.76.22.132:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gnfd/config/config.toml
```
