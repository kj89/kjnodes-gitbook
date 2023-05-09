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
peers="c4bb11ae43f4db7b8eef312a3c38861d236eb660@91.201.113.194:26656,94fdba93b79d27701896d65d8e60155e06326532@65.109.63.110:15656,d30a56dd61de5b3e8d36bf40cb0a15add3915c91@195.3.223.33:37656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14756,362ede6f335ed641e9eba0057bc1d98b391751dd@65.108.54.29:26656,7649ae1ea0dd5f640ac7dd7632a0866cf65e3aa4@31.220.90.78:26656,832f366a1429db31ca6cca1b134f304daacbb302@82.146.41.203:26656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,41681200a0e60e9477181db813e1894684020378@194.233.92.77:26656,717066f5726fb3cd7096f84911c7c8bfe5953e62@81.68.158.68:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
