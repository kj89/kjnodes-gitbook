# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

Kujira is a Layer 1 protocol built on Cosmos, which can be used for  hosting community-selected projects.

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.7.1 | **Wasm**: ON

[Website](https://kujira.app) | [Discord](https://discord.gg/teamkujira) | [Twitter](https://twitter.com/TeamKujira)

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
peers="4ae125f9c9b8e2f1ac83749c2209e26056b97851@65.108.238.103:11856,ffac364ae5a9a730b49f02ba95b11878f76b7043@135.125.189.131:31095,4c22af952c3af002136397d48f9933d0432ace7a@148.251.79.204:26656,cd11312654b4368dd2097afd468356d03a92cfe6@178.63.184.132:26656,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,129771a48f43b83c6144c7d282ad1da62434cc07@15.204.197.12:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,66778cba932969c95117cf720c1ad820fdc68ff5@65.108.235.34:26656,fc593f5f9fcf7f88790bd8274ebc791f612d3efe@65.21.89.54:26655"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.kujira/config/config.toml
```
