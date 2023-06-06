# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/agoric.png" alt=""><figcaption></figcaption></figure>

Agoric is an interoperable Proof-of-Stake chain in the Cosmos ecosystem.  Agoric JavaScript smart contract platform enables 15M+ developers across the  globe to rapidly build and deploy dapps on-chain.

**Chain ID**: agoric-emerynet-7 | **Latest Version Tag**: mainnet1B-rc2 | **Wasm**: OFF

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

**live-peers** (10)
```bash
peers="46e5e0d4b255de82e07634cf098f5ba635c1e609@65.109.23.114:14456,47cc5b7b5d448845c3c1d4914ffaa804e213129a@65.108.226.183:14456,32f7fbecd40b420d592ac460703c4ac647875566@65.109.23.238:26656,10a8ca83f9bf26d4d86a849b1576a5ea2d50dc76@148.113.142.96:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.21:27106,33b1734490b9fbbb18aef821d9e023efe99366bc@84.85.89.213:26656,a5b991654d0723e038d3723b1345b2a288d49146@38.242.156.28:26656,793955daf95ad29f003cc4ec7e6c60c00677b2f7@5.9.81.187:30656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12756,c3113bf576791a6e966fcb09fcd8773c3e51c57c@54.157.16.225:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.agoric/config/config.toml
```
