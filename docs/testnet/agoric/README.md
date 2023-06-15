# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/agoric.png" alt=""><figcaption></figcaption></figure>

Agoric is an interoperable Proof-of-Stake chain in the Cosmos ecosystem.  Agoric JavaScript smart contract platform enables 15M+ developers across the  globe to rapidly build and deploy dapps on-chain.

**Chain ID**: agoric-emerynet-8 | **Latest Version Tag**: mainnet1B-rc3 | **Wasm**: OFF

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

**live-peers** (13)
```bash
peers="793955daf95ad29f003cc4ec7e6c60c00677b2f7@5.9.81.187:30656,fbb80438d223e032a93b026517bbd2f97c0dec79@141.94.138.48:26664,33b1734490b9fbbb18aef821d9e023efe99366bc@84.85.89.213:26656,a5b991654d0723e038d3723b1345b2a288d49146@38.242.156.28:26656,7cd94fa668a6d07f15c91455c2b3f811769a6d21@35.226.248.0:26656,32f7fbecd40b420d592ac460703c4ac647875566@65.109.23.238:26656,eba8a975b3ebc338f64d8b0e146be0569ed80b74@35.238.67.135:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.21:27106,a875ef614b3902dd567be2076f18239681f24e35@82.100.58.112:26656,ae61fc38e09756a8023a80764b23e55485cba268@103.180.28.204:27656,e058557bea2bbf76756c5368406de319781a4aad@75.166.248.121:45656,0f04c4610b7511a64b8644944b907416db568590@35.222.138.81:26656,fb86a0993c694c981a28fa1ebd1fd692f345348b@34.171.162.87:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.agoric/config/config.toml
```
