# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/osmosis.png" width="150" alt=""><figcaption></figcaption></figure>

Osmosis is a DEX protocol, which means it uses smart contracts  to determine the price of digital assets, to produce liquidity  via a peer-to-peer (P2P) methodology, and to exact trades between users

**Chain ID**: osmosis-1 | **Latest Version Tag**: v15.0.0 | **Wasm**: ON

[Website](https://osmosis.zone) | [Discord](https://discord.gg/osmosis) | [Twitter](https://twitter.com/osmosiszone)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/osmosis](https://explorer.kjnodes.com/osmosis)

## Public endpoints

* api: [https://osmosis.api.kjnodes.com](https://osmosis.api.kjnodes.com)
* rpc: [https://osmosis.rpc.kjnodes.com](https://osmosis.rpc.kjnodes.com)
* grpc: osmosis.grpc.kjnodes.com:29090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@osmosis.rpc.kjnodes.com:29656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@osmosis.rpc.kjnodes.com:29659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/osmosis/addrbook.json > $HOME/.osmosisd/config/addrbook.json
```

**live-peers** (30)
```bash
peers="0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,c7fb97358712f447ca0689e814fe8c965a71b314@65.21.133.114:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,ea5ce509e09790c70609c8dc87ad4b19a0f98855@168.119.108.203:26656,4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,13d17adf418ceab5528096dcacf130830fee2b86@35.215.50.201:26656,22c0c06ee183b47d75f8d8ec6d6c63dca90c90e5@54.156.184.104:26656,f4b811759e55f665180545ad5e1b42573f660861@135.181.181.251:26656,236a60841401f53c28f7609ea50ea88feb259a1e@5.9.100.51:36656,75bae7b2af60155b6687ca3e5f92010d35cb0c12@54.164.100.216:26656,42745690b41f6a7515c4a87d88efda2e82b55b76@78.46.94.183:26656,2cb8dd6195c65458e3c18505bb70ce2ff624f85c@89.58.61.223:2000,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,a50c8dcd0e83032b5e29d5c5beef6e54ddafb508@35.83.253.164:26656,7f36123a395e902deaecf63bdaf5656bbb209623@15.204.52.75:26656,3226b67b2bb9da41b633392a785e87e8f6749939@162.55.245.149:12000,88fa3de90d06422b409ce6beb2367b94b2a1759e@51.79.17.73:26656,2d06b9ae6c8c359fb4ab84f7b88a0429d2095a6b@65.109.111.235:26656,c0c2c6ff9e456dc31c7f697c81168267dbb49339@34.83.112.45:26656,913e9db0332df1152e5afe032ab81bdb65e3f91c@110.11.23.44:26656,4d1828a3df5a7c3d05030897eb7c82e6ac79c520@135.181.138.95:12000,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,c61bf85fd330bb702b1f13f58dd3cf83c5363bf2@149.56.26.22:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@178.211.139.77:26716,a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656,ec929701754be057fb38c824fc127e26add9c900@138.201.121.185:26666,34340a9151d4a97a850d2cd64d8778279faf3f96@194.163.181.100:26656,c13125d0a7430de9448c97eea231e7dcab897df5@188.34.191.2:26756,08858368c73d4f06af2ec438457455d7cce0554f@40.76.143.93:26656,3e874613919a6f8b3fc26071fef563c88f031b3c@116.202.236.59:31656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
