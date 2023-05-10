# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/celestia.png" alt=""><figcaption></figcaption></figure>

Celestia is a minimal blockchain that only orders and publishes transactions and  does not execute them. By decoupling the consensus and application execution layers,  Celestia modularizes the blockchain technology stack and unlocks new possibilities  for decentralized application builders.

**Chain ID**: blockspacerace-0 | **Latest Version Tag**: v0.13.0 | **Wasm**: OFF

[Website](https://celestia.org) | [Discord](https://discord.gg/celestiacommunity) | [Twitter](https://twitter.com/CelestiaOrg)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/celestia-testnet](https://explorer.kjnodes.com/celestia-testnet)

## Public endpoints

* api: [https://celestia-testnet.api.kjnodes.com](https://celestia-testnet.api.kjnodes.com)
* rpc: [https://celestia-testnet.rpc.kjnodes.com](https://celestia-testnet.rpc.kjnodes.com)
* grpc: celestia-testnet.grpc.kjnodes.com:12090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@celestia-testnet.rpc.kjnodes.com:12056
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@celestia-testnet.rpc.kjnodes.com:12059
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/celestia-testnet/addrbook.json > $HOME/.celestia-app/config/addrbook.json
```

**live-peers** (11)
```bash
peers="02241bb63c01fb52033029f7155c3db5d7846c1f@168.119.64.26:26656,461f037ebd0c671f26fbad2afe74c43d285de08e@15.235.87.88:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12056,46d3f4a8341c4523f4cafc778075688022280973@95.217.113.104:26656,a1b78a15e9a66f38903d66d019f9fb6c3066f936@31.220.87.65:26656,2b8f5b788108c593378ce0dad8faff180b854cb4@185.56.139.86:26656,6fbb911f2d20d86a77ecb8b8e95f6e80cfb62548@144.76.236.211:26656,10297d22a2f1f66bfb9f2c8f7d7152660bfffd92@65.109.32.148:26116,0096a95343de3097594ebebc66542ed4a4167f2a@65.109.159.227:26656,3ef426538e3b8bfa274aa9a442583bbbda71942f@185.144.99.12:26656,00a7e4228936c514fa7e9df6466ddad0d08cbef2@18.191.143.132:31380"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
