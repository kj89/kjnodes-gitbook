# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/mars.png" width="150" alt=""><figcaption></figcaption></figure>

Mars is a credit protocol for the future: non-custodial,  open-source, transparent, algorithmic and community-governed.

**Chain ID**: mars-1 | **Latest Version Tag**: v1.0.0 | **Wasm**: ON

[Website](https://marsprotocol.io) | [Discord](https://discord.gg/marsprotocol) | [Twitter](https://twitter.com/mars_protocol)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/mars/marsvaloper1p9t4gr40rnpdwqacxgcqp7ffrfw908nu020g4n)

## Restake

[Restake with kjnodes](https://restake.app/mars/marsvaloper1p9t4gr40rnpdwqacxgcqp7ffrfw908nu020g4n) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/mars](https://explorer.kjnodes.com/mars)

## Public endpoints

* api: [https://mars.api.kjnodes.com](https://mars.api.kjnodes.com)
* rpc: [https://mars.rpc.kjnodes.com](https://mars.rpc.kjnodes.com)
* grpc: [https://mars.grpc.kjnodes.com](https://mars.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@mars.rpc.kjnodes.com:45656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@mars.rpc.kjnodes.com:45659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/mars/addrbook.json > $HOME/.mars/config/addrbook.json
```

**live-peers** (10)
```bash
peers="6685404829bcbf1b8505dfcb0600c79fde44b7bb@49.12.216.13:26656,76969af1bccdd4dcc511741b171c3d4ccb837ba6@146.59.85.223:18556,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:45656,d2a2c21754be65ad4a4f1de1f6163f681a6e8af8@192.99.44.79:18556,eff52a6fcf2634ce1d60c1a5d38809718e22c5d2@23.88.69.22:28766,f70ee212c0b3b60e0e8411ec1b978c7826f220a2@85.190.254.14:27656,be7d56127ef887d095b2f55f09be5fee1969d922@146.59.52.48:18095,1193253f91a64aa3980df627d20f620c4cbb5ec5@34.83.213.40:26656,be494851610016cff8853796a99c3ad46d8d1b5b@65.108.76.242:36095,b88814bddfccd85289d7201bfd6fc6c4b3342ab2@178.162.165.193:36095"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
