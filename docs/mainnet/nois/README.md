# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nois.png" alt=""><figcaption></figcaption></figure>

Nois Network aims to bring randomness (or noise)  to the Cosmos ecosystem by providing a safe and  secure entropy source and distributing randomness  in the form of random beacons to other Cosmos blockchains via IBC.

**Chain ID**: nois-1 | **Latest Version Tag**: v1.0.0 | **Wasm**: ON

[Website](https://nois.network) | [Discord](https://discord.gg/dHdpwtEb6F) | [Twitter](https://twitter.com/NoisRNG)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/nois/noisvaloper1fe7ju873fkknmfrmytaft93y5rlf0xcrqtp39k)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/nois/noisvaloper1fe7ju873fkknmfrmytaft93y5rlf0xcrqtp39k) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/nois](https://explorer.kjnodes.com/nois)

## Public endpoints

* api: [https://nois.api.kjnodes.com](https://nois.api.kjnodes.com)
* rpc: [https://nois.rpc.kjnodes.com](https://nois.rpc.kjnodes.com)
* grpc: nois.grpc.kjnodes.com:51090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@nois.rpc.kjnodes.com:51656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@nois.rpc.kjnodes.com:51659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nois/addrbook.json > $HOME/.noisd/config/addrbook.json
```

**live-peers** (30)
```bash
peers="a5224f7375f156c07c28f336355e4e727699fad5@65.109.95.26:27656,2e1d9305a5be27fc708ea7bc2fade939be1259e6@65.108.82.62:51656,483678c263d8ceb45b11e450628928d05c641187@194.163.167.138:60656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:51656,f03752476d5f328b26960e20b6101a68c3c9cd6d@65.109.112.170:27656,95eeb1ac374e4144b05b36f6c5986472e7ef698f@135.181.209.51:26786,7bd2beda636ef3077d349a0bacf6fca87c8d9b65@144.76.63.67:26806,0ede37f273933f5f9d6644f68e51128c6332c431@65.108.11.234:26656,922d90c7ef1840c984fcfa387a491c8d3c4481dc@65.108.141.109:55656,c86b0c3ffb4fa65b188ac68d2872a9d91559bce1@65.21.55.133:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.136:27286,563162895c3152ba7c46b115cd79f5d75017e9dc@65.108.138.80:17356,eedbb7c59906baea1aed6acb361c78f198e38c86@65.109.52.115:51656,763f4cd38f0685616b6657d9a34c1cdbf01ca90c@212.23.222.109:26456,83e530ade685efa61579eccd9f990462cd0ff36e@5.189.157.124:21656,acf21becb9397db3dc7ad29cd11993c8869d0ad3@65.21.52.246:26656,6eb54f48d03c2da8ab354c99ba25c80ccdeb5127@37.27.0.53:26656,8ec2fee6c37c07cc5af57ec870015a0191d4707d@65.108.65.36:51656,c98c58a8cd821f8814bb995d30299e76abb485aa@142.132.194.157:26456,b26e5ac4afbadf96ad31ee3aeb5e6557f2894037@65.108.199.222:30656,1893178693fc4e376f8c093ae30e44e27619f79c@198.244.213.94:25156,00852ba0bfdf20aac74369b1a5c43e50668c9738@135.181.128.114:17356,0cf59ab91e4a96d6e5427d903644edd18d9421d1@142.132.248.138:26786,379c0e32463be66e5cf8d13d62eb87ddb1a702c2@142.132.152.46:47656,2eec0137328523738936d50b0e0f08deb42da7f4@138.201.204.5:38656,7b7afef902cf7b10791c42b493b2c61a7e8b2c6a@65.21.225.10:19656,dd7607ce23081b71310137221ebe4610c3114bea@57.128.20.163:17356,6ef1914f30ac7becdf2c718b65c61cd618b7021a@57.128.144.242:26656,79d98c9f14f9b4281e3431b8f292b9ce2bc231e8@109.123.251.49:26656,f3dd2be8fa9b6fcd55236523ff30beee00f89796@135.181.252.92:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.noisd/config/config.toml
```
