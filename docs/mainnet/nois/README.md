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
* grpc: nois.grpc.kjnodes.com:15190

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@nois.rpc.kjnodes.com:15156
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@nois.rpc.kjnodes.com:15159
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nois/addrbook.json > $HOME/.noisd/config/addrbook.json
```

**live-peers** (29)
```bash
peers="3daa2128d58d812f63a0c0cf5d19aeb14f811928@65.109.28.226:03656,7bd2beda636ef3077d349a0bacf6fca87c8d9b65@144.76.63.67:26806,83e530ade685efa61579eccd9f990462cd0ff36e@5.189.157.124:21656,1f11007b46c24a24cdceba685e6c47d783ba2a09@46.4.50.247:51656,eeb51b9e6c7d6de977e3c6419f3bba78263b4b7e@192.99.32.49:26656,8ec2fee6c37c07cc5af57ec870015a0191d4707d@65.108.65.36:51656,3c5926d0b4b8750f16f6495063e6d762b2556d1e@65.21.122.47:27656,6eb54f48d03c2da8ab354c99ba25c80ccdeb5127@37.27.0.53:26656,9d21af60ad2568ffcb55a0bd0eb03b6cfa2644c5@49.12.120.113:26656,2e1d9305a5be27fc708ea7bc2fade939be1259e6@65.108.82.62:51656,171b9d4700909ec297641aa8a69d45b4149f0d1d@141.94.193.28:55726,9620f8453f34270be5fa3d458968d8bd1c997430@95.70.184.178:29656,483678c263d8ceb45b11e450628928d05c641187@194.163.167.138:60656,dd7607ce23081b71310137221ebe4610c3114bea@57.128.20.163:17356,922d90c7ef1840c984fcfa387a491c8d3c4481dc@65.108.141.109:55656,c86b0c3ffb4fa65b188ac68d2872a9d91559bce1@65.21.55.133:26656,00852ba0bfdf20aac74369b1a5c43e50668c9738@135.181.128.114:17356,c98c58a8cd821f8814bb995d30299e76abb485aa@142.132.194.157:26456,95eeb1ac374e4144b05b36f6c5986472e7ef698f@135.181.209.51:26786,6ef1914f30ac7becdf2c718b65c61cd618b7021a@57.128.144.242:26656,b26e5ac4afbadf96ad31ee3aeb5e6557f2894037@65.108.199.222:30656,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.136:27286,1893178693fc4e376f8c093ae30e44e27619f79c@198.244.213.94:25156,e409b5ae06ff0917de94f1fb636fd833ddaf9810@51.89.98.102:55726,f03752476d5f328b26960e20b6101a68c3c9cd6d@65.109.112.170:27656,763f4cd38f0685616b6657d9a34c1cdbf01ca90c@212.23.222.109:26456,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:51656,2b584d00e598766c5fd2b8e80513fef1e2cf5393@192.95.30.128:26656,ad53e98a88aa0c6f724b457ad6575b83c5f4a02b@167.235.15.19:30656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.noisd/config/config.toml
```
