# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gravitybridge.png" width="150" alt=""><figcaption></figcaption></figure>

An open, decentralized bridge that unlocks the power of  interoperability & liquidity between blockchain ecosystems.

**Chain ID**: gravity-bridge-3 | **Latest Binary Version**: v1.7.2 | **Wasm**: OFF

Website: [https://www.gravitybridge.net](https://www.gravitybridge.net)

## Restake

[Restake with kjnodes](https://restake.app/gravitybridge/gravityvaloper1nw3uavthnjwsgrrjzav2wdg9m0pw7k4fc7hvlz) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://gravitybridge.rpc.kjnodes.com](https://gravitybridge.rpc.kjnodes.com)
* api: [https://gravitybridge.api.kjnodes.com](https://gravitybridge.api.kjnodes.com)

## Peering

**state-sync**

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@gravitybridge.rpc.kjnodes.com:26656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@gravitybridge.rpc.kjnodes.com:26659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/gravitybridge/addrbook.json > $HOME/.gravity/config/addrbook.json
```

**live-peers** (10)
```
peers="16f40620f1b1942246015f35c40dd9fc84e51b01@66.94.124.27:26656,32ec6bad2b67212d2cde5e01554cd2d22940ce03@142.132.154.176:26656,5ad3fe86b1214e1f5c897d23a2863fb46bdfc1f7@185.16.38.165:14256,0b0f045fb385118c3a8f32138748922ac6358103@66.172.36.133:12656,3c514107f9bfbed84e806e943e72cc602d23ff54@65.108.71.220:26656,4bebde6a1b2907bd3cc167d2802b909770cbfda1@137.184.197.230:26656,9f13103f7eb8e82c6ba18eb53ba18ed88dac6950@65.109.69.59:14256,1f43c723cb26092e20263905cbd71609d87a9c00@172.104.202.149:26656,70cf70105cee5c7778bb70d8898d5cace6dd9e43@15.235.53.86:12856,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gravity/config/config.toml
```
