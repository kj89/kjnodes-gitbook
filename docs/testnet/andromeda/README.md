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

**live-peers** (9)
```bash
peers="385bda41dc8ce86d0dd4c99d3cf371ca8fccfeb6@135.125.189.131:20095,04f999a256386af81147442b05ffd4022313de2c@146.190.116.68:20156,b2bdcd106645c538f86f24f7a3f253d8e1bf34ab@217.76.57.54:26656,e61f287d51edab6f6dbe00a8b804614443ee6f82@80.85.242.117:26656,62f7aaafd73816bdaf685a6270541c1d1f8162ad@155.133.27.170:26656,815e9378b05a40e4a774223b55f5c6b8457a1c79@31.220.79.166:26656,257491189415103312bcd203b1c6cd114d2cde9e@38.242.225.252:26656,d0ef5f5583ff0343ea41962f68010bff54caafde@212.90.121.45:30656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
