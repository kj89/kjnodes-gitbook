# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

Kujira is a Layer 1 protocol built on Cosmos, which can be used for  hosting community-selected projects.

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.7.1 | **Wasm**: ON

Website: [https://kujira.app](https://kujira.app)

## Restake

[Restake with kjnodes](https://restake.app/kujira/kujiravaloper1tnuqj73jfn3724lqz34c27tuv80nv336sadqym) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://kujira.rpc.kjnodes.com](https://kujira.rpc.kjnodes.com)
* api: [https://kujira.api.kjnodes.com](https://kujira.api.kjnodes.com)

## Peering

**state-sync**

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@kujira.rpc.kjnodes.com:13656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@kujira.rpc.kjnodes.com:13659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/kujira/addrbook.json > $HOME/.kujira/config/addrbook.json
```

**live-peers** (10)
```
peers="c1a740841a6dc0b56730e975b1a4aa2d8c73b204@65.108.237.233:29656,ccffabe81f2de8a81e171f93fe1209392bf9993f@65.108.234.59:26656,66778cba932969c95117cf720c1ad820fdc68ff5@65.108.235.34:26656,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,6212f700687500f96ef56af3488e99fc4b009e19@212.68.34.95:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,0cb9d54761ca14006daad4442378f2a1335de6ad@65.21.121.118:26656,9ab0d2b9cd38c050d384a942208010e46e51f7d4@144.76.71.47:26656,8abdc219a07d10661ec725254354f6eb535ff039@85.10.244.234:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.kujira/config/config.toml
```
