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

**live-peers** (11)
```bash
peers="c089b582977f015b7ee1ff357a9ca7c07f6341ca@135.181.221.186:31656,04f999a256386af81147442b05ffd4022313de2c@146.190.116.68:20156,57accd1be23702a5b374f84e990d85e4ddac47c8@142.132.237.91:20156,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,385bda41dc8ce86d0dd4c99d3cf371ca8fccfeb6@135.125.189.131:20095,717066f5726fb3cd7096f84911c7c8bfe5953e62@81.68.158.68:26656,e95899eb682e517d74449dd575073daf1a3266d5@135.181.208.169:27656,56f709e56ef9e95fcfd9376e28f4afdd1178ca09@65.109.30.90:38656,41681200a0e60e9477181db813e1894684020378@194.233.92.77:26656,e61f287d51edab6f6dbe00a8b804614443ee6f82@80.85.242.117:26656,d0ef5f5583ff0343ea41962f68010bff54caafde@212.90.121.45:30656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
