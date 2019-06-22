#pragma once

#include <functional>
#include <memory>
#include <QtCore/QObject>

namespace QMatrixClient
{
    class Connection;

    class EncryptionManager: public QObject
    {
        Q_OBJECT

        public:
            // TODO: store constats separately?
            // TODO: 0.5 oneTimeKeyThreshold instead of 0.1?
            explicit EncryptionManager(const QByteArray& encryptionAccountPickle, float signedKeysProportion = 1, float oneTimeKeyThreshold = float(0.1),
                                       QObject* parent = nullptr);
            ~EncryptionManager();

            void uploadIdentityKeys(Connection* connection);
            void uploadOneTimeKeys(Connection* connection, bool forceUpdate = false);

        private:
            class Private;
            std::unique_ptr<Private> d;

    };

}  // namespace QMatrixClient