# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/agoric.png" width="150" alt=""><figcaption></figcaption></figure>

Agoric is an interoperable Proof-of-Stake chain in the Cosmos ecosystem.  Agoric JavaScript smart contract platform enables 15M+ developers across the  globe to rapidly build and deploy dapps on-chain.

**Chain ID**: agoric-emerynet-5 | **Latest Version Tag**: pismoA | **Wasm**: OFF

[Website](https://agoric.com) | [Discord](https://discord.com/invite/qDW8DRes4s) | [Twitter](https://twitter.com/agoric)


## Public endpoints

* rpc: [https://agoric-testnet.rpc.kjnodes.com](https://agoric-testnet.rpc.kjnodes.com)
* api: [https://agoric-testnet.api.kjnodes.com](https://agoric-testnet.api.kjnodes.com)

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

**live-peers** (20)
```bash
peers="a875ef614b3902dd567be2076f18239681f24e35@185.146.148.112:26656,6644a86094a0cb0152f83aed74357c439657770b@185.239.209.79:26656,32f7fbecd40b420d592ac460703c4ac647875566@65.109.23.238:26656,7b1cafa0879374125c623d854bcc0cb9cd98729e@185.213.25.151:26656,e5d3db7a51d3fb40a4855d6677318944faf7d5f2@142.132.191.166:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:27656,3f4e87ddb2e61fdd01398c071fa986259f096334@209.34.205.57:26656,4dee5e4456307469d037c35eb0157f1f252b3f99@135.181.35.255:26656,6f9e22eba0130f1a29c25e28beeae69b2621a403@35.226.248.0:26656,a5b991654d0723e038d3723b1345b2a288d49146@38.242.156.28:26656,fd9d8063921531990cfebb72d5adadf276484e8d@13.215.217.74:26656,793955daf95ad29f003cc4ec7e6c60c00677b2f7@5.9.81.187:30656,c72d05f83b53dc7f6c55d7d3e67c304716d27d80@116.202.227.117:27656,8dfb920cdc2eba42b688f44fdd26e12dabfbb6a9@95.217.130.111:27656,a3a1e6c7a9ceec632c22769a9e369d05a796dc24@65.108.79.246:26709,fb86a0993c694c981a28fa1ebd1fd692f345348b@35.238.67.135:26656,98e1069b1cfc445e377eda6a0eadd94f7877065d@162.55.169.76:26656,53ae0b0710f2f32aa60717953a51e60a7ad7b1c5@35.226.207.157:26656,42084028a65c5d609793ffc618d1dcbf374fc301@65.109.28.219:14456,c63cc83797e108ee7881209dd1545671a5e92ea6@34.71.23.243:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.agoric/config/config.toml
```
