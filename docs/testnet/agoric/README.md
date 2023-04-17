# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/agoric.png" width="150" alt=""><figcaption></figcaption></figure>

Agoric is an interoperable Proof-of-Stake chain in the Cosmos ecosystem.  Agoric JavaScript smart contract platform enables 15M+ developers across the  globe to rapidly build and deploy dapps on-chain.

**Chain ID**: agoric-emerynet-5 | **Latest Version Tag**: pismoC | **Wasm**: OFF

[Website](https://agoric.com) | [Discord](https://discord.com/invite/qDW8DRes4s) | [Twitter](https://twitter.com/agoric)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/agoric-testnet](https://explorer.kjnodes.com/agoric-testnet)

## Public endpoints

* api: [https://agoric-testnet.api.kjnodes.com](https://agoric-testnet.api.kjnodes.com)
* rpc: [https://agoric-testnet.rpc.kjnodes.com](https://agoric-testnet.rpc.kjnodes.com)
* grpc: agoric-testnet.grpc.kjnodes.com:27090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@agoric-testnet.rpc.kjnodes.com:27656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@agoric-testnet.rpc.kjnodes.com:27659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/agoric-testnet/addrbook.json > $HOME/.agoric/config/addrbook.json
```

**live-peers** (23)
```bash
peers="793955daf95ad29f003cc4ec7e6c60c00677b2f7@5.9.81.187:30656,70ac007461e0d912aeba6eda56ac3fed7d3087f8@135.181.85.31:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:27656,3f4e87ddb2e61fdd01398c071fa986259f096334@209.34.206.46:26656,b7a728cbf102ff45dca7d9dc5b433408e240649f@65.109.23.114:14456,a49d469686e32f6490b56a2a693e83c130f3ee2a@144.76.145.151:26656,33b1734490b9fbbb18aef821d9e023efe99366bc@84.85.89.213:26656,4dee5e4456307469d037c35eb0157f1f252b3f99@135.181.35.255:26656,7ea47a018710e43a9eafd4eebc8340d2f48eb3ba@94.130.132.227:2160,6f9e22eba0130f1a29c25e28beeae69b2621a403@35.226.248.0:26656,7b1cafa0879374125c623d854bcc0cb9cd98729e@185.213.25.151:26656,a3a1e6c7a9ceec632c22769a9e369d05a796dc24@65.108.79.246:26709,980583e1dfd16988b6fdb22dd733f3260c535e45@192.241.137.132:26656,b74a421ccb5b9928a6a1a158c26189f18319c344@65.108.226.183:14456,98e1069b1cfc445e377eda6a0eadd94f7877065d@162.55.169.76:26656,6644a86094a0cb0152f83aed74357c439657770b@185.239.209.79:26656,dfaff8b84e30a30732757b1bcaa5463746dbc87b@34.30.233.82:26656,8dfb920cdc2eba42b688f44fdd26e12dabfbb6a9@95.217.130.111:27656,dd9944850a69276f81792b0c0ebdbeee17df5e5e@34.69.172.140:26656,a875ef614b3902dd567be2076f18239681f24e35@82.100.58.112:26656,c72d05f83b53dc7f6c55d7d3e67c304716d27d80@116.202.227.117:27656,a21bd5ae7488c18d7e6387f20ae0484acb70be01@13.215.217.74:26656,029b9018489d618e4368e9af34599e07a9fc07c9@34.67.210.29:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.agoric/config/config.toml
```
