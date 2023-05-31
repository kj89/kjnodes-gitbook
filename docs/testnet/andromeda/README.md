# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/andromeda.png" alt=""><figcaption></figcaption></figure>

Andromeda is an application platform layer that connects all  public blockchains in the Cosmos ecosystem. Through our vast  library of no-code smart contracts, users can harness the power of web3.

**Chain ID**: galileo-3 | **Latest Version Tag**: galileo-3-v1.1.0-beta1 | **Wasm**: ON

[Website](https://www.andromedaprotocol.io) | [Discord](https://discord.gg/wzM3kSN3sE) | [Twitter](https://twitter.com/andromedaprot)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/andromeda-testnet](https://explorer.kjnodes.com/andromeda-testnet)

## Public endpoints

* api: [https://andromeda-testnet.api.kjnodes.com](https://andromeda-testnet.api.kjnodes.com)
* rpc: [https://andromeda-testnet.rpc.kjnodes.com](https://andromeda-testnet.rpc.kjnodes.com)
* grpc: andromeda-testnet.grpc.kjnodes.com:14790

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@andromeda-testnet.rpc.kjnodes.com:14756
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@andromeda-testnet.rpc.kjnodes.com:14759
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/andromeda-testnet/addrbook.json > $HOME/.andromedad/config/addrbook.json
```

**live-peers** (10)
```bash
peers="3969b8ddc6d0ed9f2deb0265e4b26e88c5cb894a@149.102.150.250:30656,008284cce007a3bdf77a6a54bfb7654490405e1c@185.197.251.180:26656,a537cc2879fc79401f6834aa6483fbb1dee18ef0@137.184.44.33:20156,d78df88bc4a487c140e466a23f549ed90e7ebfb6@161.97.152.157:27656,537e0302400604f7dd1b8e49c5660da311066610@199.175.98.104:26656,385bda41dc8ce86d0dd4c99d3cf371ca8fccfeb6@135.125.189.131:20095,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,139e89b8868aed5c5922a563ecd5002959af04ff@65.108.111.236:55716,d66cf29d246ed98290694418545914bb8c03c78b@65.108.215.65:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
