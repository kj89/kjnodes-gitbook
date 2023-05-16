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

**live-peers** (12)
```bash
peers="c72d05f83b53dc7f6c55d7d3e67c304716d27d80@116.202.227.117:27656,8dfb920cdc2eba42b688f44fdd26e12dabfbb6a9@95.217.130.111:27656,4dee5e4456307469d037c35eb0157f1f252b3f99@135.181.35.255:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12756,980583e1dfd16988b6fdb22dd733f3260c535e45@192.241.137.132:26656,10a8ca83f9bf26d4d86a849b1576a5ea2d50dc76@57.128.86.7:26656,70ac007461e0d912aeba6eda56ac3fed7d3087f8@135.181.85.31:26656,33b1734490b9fbbb18aef821d9e023efe99366bc@84.85.89.213:26656,98e1069b1cfc445e377eda6a0eadd94f7877065d@162.55.169.76:26656,9853ad6e5a8db4bf4201d90f5f4d049baf32833e@54.209.171.126:26656,793955daf95ad29f003cc4ec7e6c60c00677b2f7@5.9.81.187:30656,029b9018489d618e4368e9af34599e07a9fc07c9@34.67.193.183:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.agoric/config/config.toml
```
