# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/gravitybridge.png" width="150" alt=""><figcaption></figcaption></figure>

An open, decentralized bridge that unlocks the power of  interoperability & liquidity between blockchain ecosystems.

**Chain ID**: gravity-bridge-3 | **Latest Version Tag**: v1.8.1 | **Wasm**: OFF

[Website](https://www.gravitybridge.net) | [Discord](https://discord.gg/ARV8dTSjAk) | [Twitter](https://twitter.com/gravity_bridge)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/gravitybridge/gravityvaloper1nw3uavthnjwsgrrjzav2wdg9m0pw7k4fc7hvlz)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/gravitybridge/gravityvaloper1nw3uavthnjwsgrrjzav2wdg9m0pw7k4fc7hvlz) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/gravitybridge](https://explorer.kjnodes.com/gravitybridge)

## Public endpoints

* api: [https://gravitybridge.api.kjnodes.com](https://gravitybridge.api.kjnodes.com)
* rpc: [https://gravitybridge.rpc.kjnodes.com](https://gravitybridge.rpc.kjnodes.com)
* grpc: gravitybridge.grpc.kjnodes.com:26090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@gravitybridge.rpc.kjnodes.com:26656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@gravitybridge.rpc.kjnodes.com:26659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/gravitybridge/addrbook.json > $HOME/.gravity/config/addrbook.json
```

**live-peers** (8)
```bash
peers="16f40620f1b1942246015f35c40dd9fc84e51b01@66.94.124.27:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:26656,db1e909b003e3d9d7565211db26295e84c4695a5@65.21.135.86:2000,572d417e11368f588d110efdeb7102a6a3c0752d@161.35.224.108:26656,975d74154848443004de90e31192186512f3423c@38.242.143.195:26656,6eb2a2e7bcd82aad56b6652a328c72f148f84935@194.147.58.224:26656,e940c7788dfbf02030d0838fb3dc9cdb21cf5832@66.94.112.81:26656,e5362a93c6e7f686d72c8d6d98be2c7bceeb5cc3@49.12.23.149:27010"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gravity/config/config.toml
```
