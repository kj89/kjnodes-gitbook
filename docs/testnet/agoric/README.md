# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/agoric.png" alt=""><figcaption></figcaption></figure>

Agoric is an interoperable Proof-of-Stake chain in the Cosmos ecosystem.  Agoric JavaScript smart contract platform enables 15M+ developers across the  globe to rapidly build and deploy dapps on-chain.

**Chain ID**: agoric-emerynet-5 | **Latest Version Tag**: pismoC | **Wasm**: OFF

[Website](https://agoric.com) | [Discord](https://discord.com/invite/qDW8DRes4s) | [Twitter](https://twitter.com/agoric)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/agoric-testnet](https://explorer.kjnodes.com/agoric-testnet)

## Public endpoints

* api: [https://agoric-testnet.api.kjnodes.com](https://agoric-testnet.api.kjnodes.com)
* rpc: [https://agoric-testnet.rpc.kjnodes.com](https://agoric-testnet.rpc.kjnodes.com)
* grpc: agoric-testnet.grpc.kjnodes.com:12790

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@agoric-testnet.rpc.kjnodes.com:12756
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@agoric-testnet.rpc.kjnodes.com:12759
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/agoric-testnet/addrbook.json > $HOME/.agoric/config/addrbook.json
```

**live-peers** (9)
```bash
peers="793955daf95ad29f003cc4ec7e6c60c00677b2f7@5.9.81.187:30656,98e1069b1cfc445e377eda6a0eadd94f7877065d@162.55.169.76:26656,33b1734490b9fbbb18aef821d9e023efe99366bc@84.85.89.213:26656,4dee5e4456307469d037c35eb0157f1f252b3f99@135.181.35.255:26656,b7a728cbf102ff45dca7d9dc5b433408e240649f@65.109.23.114:14456,8dfb920cdc2eba42b688f44fdd26e12dabfbb6a9@95.217.130.111:27656,029b9018489d618e4368e9af34599e07a9fc07c9@34.67.193.183:26656,b74a421ccb5b9928a6a1a158c26189f18319c344@65.108.226.183:14456,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.agoric/config/config.toml
```
